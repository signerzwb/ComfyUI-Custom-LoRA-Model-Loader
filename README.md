# 神都猫扩展LoRA加载及对比器

一个功能增强的ComfyUI LoRA加载工具集，支持多路径扫描、绝对路径输入，新增**批量LoRA对比**与**多提示词输入**能力，让LoRA管理更灵活。
视频操作说明：
https://www.bilibili.com/video/BV1NEsWzREU5/?vd_source=ca144c51975a3fad0691206554673079

## 核心功能

- 支持从多个自定义文件夹中扫描LoRA文件（通过配置文件管理路径）
- 允许直接输入本地绝对路径加载LoRA文件
- 仅对模型（Model）应用LoRA效果，不影响CLIP模型
- 支持正负强度调节（-10.0 ~ 10.0），满足特殊效果需求
- 自动过滤不支持的文件格式（仅识别 `.safetensors`/`.pt`/`.bin`/`.ckpt`）
- **新增批量LoRA对比**：通过列表节点一次加载多个LoRA，快速对比不同LoRA效果
- **多场景扩展输入**：列表节点也可用于单LoRA的多提示词组合输入


## 节点说明

| 节点名称 | 功能描述 |
|---------|---------|
| 神都猫扩展LoRA加载自定义文件夹(LoRA Custom List) | 从配置文件指定的多个文件夹中扫描LoRA，提供下拉列表选择 |
| 神都猫扩展LoRA自定义文件路径(LoRA Custom File Path) | 直接输入LoRA文件的绝对路径加载（适合临时加载单个文件） |
| 神都猫LoRA路径列表生成器(Lora Path List) | 支持10个独立LoRA路径输入 + 列表输入，输出路径列表，用于批量加载与效果对比 |


## 安装方法

### 方法1：通过Git克隆（推荐，方便更新）
1. 打开终端/命令提示符，进入ComfyUI的 `custom_nodes` 目录
2. 执行以下命令：
   ```bash
   git clone https://github.com/signerzwb/ComfyUI-Custom-LoRA-Model-Loader.git
   ```
3. 重启ComfyUI


### 方法2：手动下载安装
1. 访问GitHub仓库：[https://github.com/signerzwb/ComfyUI-Custom-LoRA-Model-Loader](https://github.com/signerzwb/ComfyUI-Custom-LoRA-Model-Loader)
2. 点击右上角的 `Code` 按钮，选择 `Download ZIP` 下载压缩包
3. 解压下载的ZIP文件，得到 `ComfyUI-Custom-LoRA-Model-Loader` 文件夹
4. 将该文件夹复制到ComfyUI的 `custom_nodes` 目录下
5. 重启ComfyUI


## 配置文件说明（针对"列表"版本节点）

### 配置文件路径
节点会自动查找以下位置的配置文件：
- ComfyUI工作目录下的 `lora_scan_paths.txt`
- 本节点文件夹（`ComfyUI-Custom-LoRA-Model-Loader`）下的 `lora_scan_paths.txt`


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
```


## 批量LoRA对比使用示例

通过「神都猫LoRA路径列表生成器」节点，可一次性输入多个LoRA路径，配合其他节点实现**多LoRA效果批量对比**：

1. 在列表节点中填写或连接多个LoRA文件路径
2. 将列表输出连接到支持批量LoRA加载的节点（或通过循环节点依次加载）
3. 结合图像批量生成/对比节点，快速验证不同LoRA的效果差异


## 多提示词输入扩展

「神都猫LoRA路径列表生成器」的列表输入能力，也可用于**单LoRA的多提示词组合场景**：

- 在列表中输入不同风格/细节的提示词
- 配合LoRA加载节点与图像生成节点，批量生成同一LoRA下的多提示词效果对比图


## 联系作者

- QQ：555649
- 微信：17223901（可备注入群，拉你进ComfyUI学习群）
- B站：神都猫玩AI
- QQ群：340983417
  
