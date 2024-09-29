"""以列表的形式加载一个文本文件"""

import sys

def load(file):
    """打开文件，并以列表的形式返回文件内容对应的小写字母"""
    try:
        with open(file) as in_file:
            loaded_txt=in_file.read().strip().split('\n')
            loaded_txt=[x.lower() for x in loaded_txt]
            return loaded_txt
    except IOError as e:
        print("{}\nError opening{}.Terminating program.".format(e,file),file=sys.stderr)
        sys.exit(1)