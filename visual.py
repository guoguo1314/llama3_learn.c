import torch

# 加载权重文件为字典形式
state_dict = torch.load('Meta-Llama-3-8B/original/consolidated.00.pth', map_location='cpu')

# 打印字典键（通常这些键对应模型各层的名称）
for key in state_dict.keys():
    print(key)
