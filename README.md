# 神都猫扩展LoRA加载器

一个功能增强的ComfyUI LoRA加载节点，支持自定义多路径扫描、绝对路径直接输入，让LoRA管理更灵活。


## 核心功能

- 支持从多个自定义文件夹中扫描LoRA文件（通过配置文件管理路径）
- 允许直接输入本地绝对路径加载LoRA文件
- 仅对模型（Model）应用LoRA效果，不影响CLIP模型
- 支持正负强度调节（-10.0 ~ 10.0），满足特殊效果需求
- 自动过滤不支持的文件格式（仅识别 `.safetensors`/`.pt`/`.bin`/`.ckpt`）


## 节点说明

| 节点名称 | 功能描述 |
|---------|---------|
| 神都猫扩展LoRA加载器(列表) | 从配置文件指定的多个文件夹中扫描LoRA，提供下拉列表选择 |
| 神都猫扩展LoRA加载器(lora路径) | 直接输入LoRA文件的绝对路径加载（适合临时加载单个文件） |


## 安装方法

1. 下载本节点文件夹 `ComfyUI-Model-Only-LoRA-Loader`
2. 将文件夹复制到ComfyUI的 `custom_nodes` 目录下
3. 重启ComfyUI


## 配置文件说明（针对"列表"版本节点）

### 配置文件路径
节点会自动查找以下位置的配置文件：
- ComfyUI工作目录下的 `lora_scan_paths.txt`
- 本节点文件夹（`ComfyUI-Model-Only-LoRA-Loader`）下的 `lora_scan_paths.txt`


### 配置文件格式
- 一行填写一个文件夹路径（支持绝对路径）
- 以 `#` 开头的行为注释（会被忽略）
- 空行会被自动跳过

示例：
```txt
# 这是我的LoRA文件夹配置
# 请替换为你的实际路径

D:/AI Models/LoRA/人物
D:/AI Models/LoRA/风格
E:/Stable Diffusion/自定义LoRA
