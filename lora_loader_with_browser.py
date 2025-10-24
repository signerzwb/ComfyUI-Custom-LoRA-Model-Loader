# lora_loader_with_browser.py
import os
import comfy.utils
from comfy.sd import load_lora_for_models
from .model_only_lora_loader import ModelOnlyLoraLoader  # 继承基础类
from .utils import SUPPORTED_EXTENSIONS, load_scan_paths  # 导入公共工具

class ModelOnlyLoraLoaderWithBrowser(ModelOnlyLoraLoader):
    @classmethod
    def INPUT_TYPES(s):        
        scan_paths = load_scan_paths()  # 使用公共工具函数
        lora_files = []
        for root_path in scan_paths:
            if not os.path.exists(root_path):
                continue
            for dirpath, _, filenames in os.walk(root_path):
                for filename in filenames:
                    if filename.lower().endswith(SUPPORTED_EXTENSIONS):
                        full_path = os.path.join(dirpath, filename)
                        lora_files.append(full_path)
        
        return {
            "required": {
                "lora_path": (lora_files, {
                    "placeholder": "选择或输入LoRA文件路径",
                    "label": "LoRA文件",
                    "allow_custom_value": True
                }),
                "strength_model": ("FLOAT", {
                    "default": 1.0,
                    "min": -10.0,
                    "max": 10.0,
                    "step": 0.01
                }),
            },
            "optional": {
                "model": ("MODEL",),
            }
        }
    
    CATEGORY = "loaders/custom"
    RETURN_TYPES = ("MODEL", "STRING")
    RETURN_NAMES = ("模型", "当前LoRA绝对路径")
    FUNCTION = "load_lora_to_model"

    def load_lora_to_model(self, lora_path, strength_model, model=None):
        lora_abs_path = os.path.abspath(lora_path)
        
        if not os.path.isfile(lora_path):
            raise FileNotFoundError(f"LoRA文件不存在：{lora_path}")
        if not lora_path.lower().endswith(SUPPORTED_EXTENSIONS):
            raise ValueError(f"不支持的格式：{lora_path}（需{SUPPORTED_EXTENSIONS}）")
        
        if model is not None:
            try:
                lora_data = comfy.utils.load_torch_file(lora_path, safe_load=True)
                model, _ = load_lora_for_models(
                    model, 
                    clip=None,
                    lora=lora_data,
                    strength_model=strength_model, 
                    strength_clip=0.0
                )
            except Exception as e:
                raise RuntimeError(f"LoRA加载失败：{str(e)}")
        
        return (model, lora_abs_path)