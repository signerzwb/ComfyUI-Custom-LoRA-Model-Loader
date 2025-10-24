# __init__.py
from .model_only_lora_loader import ModelOnlyLoraLoader
from .lora_loader_with_browser import ModelOnlyLoraLoaderWithBrowser
from .lora_path_list import LoraPathList

NODE_CLASS_MAPPINGS = {
    "ModelOnlyLoraLoaderWithBrowser": ModelOnlyLoraLoaderWithBrowser,
    "ModelOnlyLoraLoader": ModelOnlyLoraLoader,
    "LoraPathList": LoraPathList
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ModelOnlyLoraLoaderWithBrowser": "神都猫扩展LoRA加载自定义文件夹(LoRA Custom List)",
    "ModelOnlyLoraLoader": "神都猫扩展LoRA自定义文件路径(LoRA Custom File Path)",
    "LoraPathList": "神都猫LoRA路径列表生成器(Lora Path List)"
}