# model_only_lora_loader.py
import os
import comfy.utils
from comfy.sd import load_lora_for_models
from nodes import LoraLoader
from .utils import SUPPORTED_EXTENSIONS  # 导入公共常量

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
                    "min": -10.0,
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
            lora_data = comfy.utils.load_torch_file(lora_path, safe_load=True)
            model, _ = load_lora_for_models(
                model, 
                clip=None,
                lora=lora_data,
                strength_model=strength_model, 
                strength_clip=0.0
            )
            return (model,)
        except Exception as e:
            raise RuntimeError(f"LoRA加载失败：{str(e)}")