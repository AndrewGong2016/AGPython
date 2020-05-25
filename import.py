#!/usr/bin/python3

import sys

print('======================Python import mode================')
print('保存在sys.argv中的命令行参数：')
for i in sys.argv:
    print(i)
print('\n python 路径为: ',sys.path)
