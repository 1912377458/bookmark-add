# 用于中文标题性质的目录

# from PyPDF2 import PdfFileReader as reader, PdfFileWriter as writer
import re
import os

def toHeader(ls):
    str = ""
    for i in range(len(text)-1):str += ' '+ text[i]
    str += '\t' +text[-1] + '\n'
    return str

def store_method(store, text,count):
    store.write('\t'*count + toHeader(text))


file = open(r'bookmarks/概率论习题解析.txt', 'r')
content = file.readlines()
# 如果存在原先的文件，则删除
if os.path.exists("model.txt"):
  os.remove("model.txt")

for item in content:
    # 进行逐行的匹配
    text = re.sub(r'\s+', "#", item.strip()).split('#')
    with open('model.txt', 'a') as store:
        if re.search(r'第[一二三四五六七八九十]+章', text[0]):
            # 作为一级标题，不需要缩进
            store_method(store, text, 0)
        elif re.search(r'第[一二三四五六七八九十]+节', text[0]):
            # 小节作为二级标题，需要有一个缩进
            store_method(store, text, 1)
        elif re.search(r'^[一二三四五六七八九十]+', text[0]):
            # 三级标题，需要两个缩进
            store_method(store, text, 2)
        elif re.search(r'^[0-9]+', text[0]):
            # 四级标题，三个缩进
            store_method(store, text, 3)
        else:
            # 上述情况都不满足，那就直接作为一级标题
            store_method(store, text, 0)
