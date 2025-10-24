# lora_path_list.py
class LoraPathList:
    @classmethod
    def INPUT_TYPES(cls):
        # 构建10个LoRA路径输入项
        required_inputs = {}
        for i in range(1, 11):
            required_inputs[f"lora_path_{i}"] = (
                "STRING", 
                {
                    "multiline": False, 
                    "default": "",
                    "placeholder": f"输入第{i}个LoRA文件路径",
                    "label": f"LoRA路径_{i}"
                }
            )
        
        return {
            "required": required_inputs,
            "optional": {
                "optional_lora_list": ("STRING_LIST", {
                    "default": [],
                    "placeholder": "输入额外的LoRA路径列表",
                    "label": "额外LoRA列表"
                })
            }
        }

    RETURN_TYPES = ("STRING_LIST", "STRING")
    RETURN_NAMES = ("lora_paths_list", "lora_paths_strings")
    OUTPUT_IS_LIST = (False, True)
    FUNCTION = "run"
    CATEGORY = "loaders/custom"

    def run(self, **kwargs):
        lora_paths = []

        # 处理可选的列表输入
        if "optional_lora_list" in kwargs and kwargs["optional_lora_list"]:
            for path in kwargs["optional_lora_list"]:
                if path and isinstance(path, str):
                    lora_paths.append(path.strip())

        # 处理10个单独的路径输入
        for i in range(1, 11):
            key = f"lora_path_{i}"
            if key in kwargs:
                path = kwargs[key].strip()
                if path:
                    lora_paths.append(path)

        return (lora_paths, lora_paths)