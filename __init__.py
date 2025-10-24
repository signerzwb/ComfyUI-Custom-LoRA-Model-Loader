import os
import comfy.utils
from comfy.sd import load_lora_for_models
from nodes import LoraLoader  # 引入官方基础类

# 支持的LoRA文件扩展名
SUPPORTED_EXTENSIONS = ('.safetensors', '.pt', '.bin', '.ckpt')  # 涵盖常见格式

# 读取路径配置文件（不存在则报错）
def load_scan_paths(config_file="lora_scan_paths.txt"):
    """从txt文件读取扫描路径，一行一个路径，文件不存在则报错"""
    scan_paths = []
    # 查找配置文件可能的位置（当前目录和节点所在目录）
    possible_paths = [
        config_file,  # 当前工作目录
        os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file)  # 节点所在目录
    ]
    
    # 检查是否存在配置文件
    found_path = None
    for path in possible_paths:
        if os.path.exists(path) and os.path.isfile(path):
            found_path = path
            break
    
    # 不存在则直接报错
    if not found_path:
        raise FileNotFoundError(f"没有找到配置路径文件“{config_file}”，请在节点目录或工作目录创建该文件并配置路径")
    
    # 读取配置文件内容
    with open(found_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # 跳过空行和注释行
            if not line or line.startswith('#'):
                continue
            # 检查路径是否存在（仅提示，不强制过滤，允许配置未创建的路径）
            if not os.path.exists(line):
                print(f"警告：配置文件中的路径不存在 - {line}")
            scan_paths.append(line)
    
    return scan_paths

# 基础的仅模型LoRA加载器（父类）
class ModelOnlyLoraLoader(LoraLoader):
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "model": ("MODEL",),
                "lora_path": ("STRING", {
                    "default": "",
                    "placeholder": "输入LoRA文件完整路径",
                    "label": "LoRA文件路径"
                }),
                "strength_model": ("FLOAT", {
                    "default": 1.0,
                    "min": -10.0,  # 支持负强度效果
                    "max": 10.0,
                    "step": 0.01
                }),
            }
        }
    
    CATEGORY = "loaders/custom"
    RETURN_TYPES = ("MODEL",)
    FUNCTION = "load_lora_to_model"

    def load_lora_to_model(self, model, lora_path, strength_model):
        if not os.path.isfile(lora_path):
            raise FileNotFoundError(f"LoRA文件不存在：{lora_path}")
        if not lora_path.lower().endswith(SUPPORTED_EXTENSIONS):
            raise ValueError(f"不支持的格式：{lora_path}（需{SUPPORTED_EXTENSIONS}）")
        
        try:
            # 使用ComfyUI内置工具加载LoRA文件（兼容各种格式）
            lora_data = comfy.utils.load_torch_file(lora_path, safe_load=True)
            # 移除device参数（当前版本ComfyUI已不需要手动指定）
            model, _ = load_lora_for_models(
                model, 
                clip=None,  # 不处理CLIP模型
                lora=lora_data,
                strength_model=strength_model, 
                strength_clip=0.0  # CLIP强度强制为0
            )
            return (model,)
        except Exception as e:
            raise RuntimeError(f"LoRA加载失败：{str(e)}")


# 带文件浏览器的子类
class ModelOnlyLoraLoaderWithBrowser(ModelOnlyLoraLoader):
    @classmethod
    def INPUT_TYPES(s):        
        # 从配置文件加载扫描路径（不存在会直接报错）
        scan_paths = load_scan_paths()
        
        # 扫描指定路径下的LoRA文件
        lora_files = []
        for root_path in scan_paths:
            if not os.path.exists(root_path):
                continue  # 跳过不存在的路径
            for dirpath, _, filenames in os.walk(root_path):
                for filename in filenames:
                    if filename.lower().endswith(SUPPORTED_EXTENSIONS):
                        full_path = os.path.join(dirpath, filename)
                        lora_files.append(full_path)
        
        return {
            "required": {
                "model": ("MODEL",),
                "lora_path": (lora_files, {
                    "placeholder": "选择或输入LoRA文件路径",
                    "label": "LoRA文件",
                    "allow_custom_value": True  # 允许手动输入路径
                }),
                "strength_model": ("FLOAT", {
                    "default": 1.0,
                    "min": -10.0,
                    "max": 10.0,
                    "step": 0.01
                }),
            }
        }
    
    CATEGORY = "loaders/custom"
    RETURN_TYPES = ("MODEL",)
    FUNCTION = "load_lora_to_model"  # 复用父类的加载方法


# 注册节点
NODE_CLASS_MAPPINGS = {
    "ModelOnlyLoraLoaderWithBrowser": ModelOnlyLoraLoaderWithBrowser,
    "ModelOnlyLoraLoader": ModelOnlyLoraLoader  # 同时注册基础版节点
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ModelOnlyLoraLoaderWithBrowser": "神都猫扩展LoRA加载自定义文件夹(LoRA Custom List)",
    "ModelOnlyLoraLoader": "神都猫扩展LoRA自定义文件路径(LoRA Custom File Path)"
}