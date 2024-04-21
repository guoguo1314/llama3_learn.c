#模型下载
from modelscope import snapshot_download
model_dir = snapshot_download('huangjintao/Meta-Llama-3-8B',cache_dir='/mnt/workspace/llama3.c')