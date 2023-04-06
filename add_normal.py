import re
import os

def toHeader(ls):
    str = ""
    for i in range(len(text)-1):str += ' '+ text[i]
    str += '\t' +text[-1] + '\n'
    return str


file = open(r'bookmarks/24计网.txt', 'r')
content = file.readlines()
# 如果存在原先的文件，则删除
if os.path.exists("model.txt"):
  os.remove("model.txt")
for item in content:
    with open('model.txt', 'a') as store:
        text = re.sub(r'\s+', "#", item.strip()).split('#')
        if re.search(r'^第\d+章$', text[0]):
            store.write(toHeader(text))
        elif re.search(r'\d.+',text[0]):
            # 此时根据点的个数确定标题等级（点的个数加1）
            level = text[0].count('.')
            store.write('\t'*level + toHeader(text))
        else:
            # 都不匹配
            if len(text) == 3:
                store.write(toHeader(text))
            else:
                store.write(toHeader(text))