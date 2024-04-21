**Notice：**
This code  built on [llama2.c ](https://github.com/karpathy/llama2.c) for Inference deployment of the llama3,  where convert-tokenizer-llama3.py is [distribution-llama](https://github.com/b4rtaz/distributed-llama). The code explanation can be found on [this page](https://blog.csdn.net/qq_44576434?spm=1000.2115.3001.5343).<br>
For Chinese version, see [知乎](https://zhuanlan.zhihu.com/p/693700723)<br>
First time open source, please point out any errors.

## 1. download model
For CN,点[它](https://zhuanlan.zhihu.com/p/693541231)试试

## 2. clone code
    git clone https://github.com/guoguo1314/llama3_learn.c.git
    cd llama3_learn.c
## 3. convert tokenizer
    python convert-tokenizer-llama3.py tokenizer.model


## 4. convert model
    python convert-llama3.py Meta-Llama-3-8B/original llama3_8.bin

## 5. run
    make run
    ./run llama3_8.bin

## 6. appreciate
Finally, thank you [karpathy,](https://github.com/karpathy) [b4rtaz](https://github.com/b4rtaz) open source, I don't know if you can see.
