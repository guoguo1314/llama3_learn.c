import sys
import struct
import base64

# Format of input file:
# ```
# IQ== 0
# Ig== 1
# Iw== 2
# ...
# ```

nSpecialTokens = 256
specialTokens = [
    '<|begin_of_text|>',
    '<|end_of_text|>',
    '<|reserved_special_token_0|>',
    '<|reserved_special_token_1|>',
    '<|reserved_special_token_2|>',
    '<|reserved_special_token_3|>',
    '<|start_header_id|>',
    '<|end_header_id|>',
    '<|reserved_special_token_4|>',
    '<|eot_id|>',
] + [
    f'<|reserved_special_token_{i}|>'
    for i in range(5, nSpecialTokens - 5)
]

if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print('Invalid usage')
        exit(1)

    modelPath = sys.argv[1]

    with open(modelPath, 'r') as inputFile:
        with open('llama3-tokenizer.bin', 'wb') as outputFile:
            inputLines = inputFile.readlines()
            nLines = len(inputLines)
            outputFile.write(struct.pack('I', nLines + nSpecialTokens))
            for line in inputLines:
              # 将行拆分为s[0]（base64编码的令牌）和s[1]（负数分数）
                s = line.split(' ')
                bytes = base64.b64decode(s[0])
                score = -float(s[1])
                outputFile.write(struct.pack('fI', score, len(bytes)))
                outputFile.write(bytes)
            specialTokenIndex = nLines
          # 处理并写入特殊令牌
            for token in specialTokens:
                bytes = token.encode('utf-8')
                score = -float(specialTokenIndex)
                outputFile.write(struct.pack('fI', score, len(bytes)))
                outputFile.write(bytes)
                specialTokenIndex += 1
            print(f'vocab_size={specialTokenIndex}')