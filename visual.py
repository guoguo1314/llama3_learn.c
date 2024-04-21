import torch

# 加载模型权重文件
model = torch.load('/mnt/workspace/llama3.c/download/Meta-Llama-3-8B/original/consolidated.00.pth')

# 查看模型结构和包含的层
print(model)