# utils.py
import os

SUPPORTED_EXTENSIONS = ('.safetensors', '.pt', '.bin', '.ckpt')

def load_scan_paths(config_file="lora_scan_paths.txt"):
    scan_paths = []
    possible_paths = [
        config_file,
        os.path.join(os.path.dirname(os.path.abspath(__file__)), config_file)
    ]
    
    found_path = None
    for path in possible_paths:
        if os.path.exists(path) and os.path.isfile(path):
            found_path = path
            break
    
    if not found_path:
        raise FileNotFoundError(f"没有找到配置路径文件“{config_file}”，请在节点目录或工作目录创建该文件并配置路径")
    
    with open(found_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if not os.path.exists(line):
                print(f"警告：配置文件中的路径不存在 - {line}")
            scan_paths.append(line)
    
    return scan_paths