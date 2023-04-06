# 进行目录的处理，根据缩进级别对应不同的标题等级
from PyPDF2 import PdfFileReader as reader, PdfFileWriter as writer

pdf_path = r'/Users/xiangyu/Downloads/21080480.pdf'  # 要处理的pdf
pdf_in = reader(pdf_path)
pdf_out = writer()
# 将读取的pdf放到writer中
pageCount = pdf_in.getNumPages()
for iPage in range(pageCount):
    pdf_out.addPage(pdf_in.getPage(iPage))
# 读取存储的目录
ls = [[], [], [],[],[]]  # 用于存放多级目录
offset = 5 # 偏移值，计算方法为pdf页码减去实际页码再减一
file = open('model.txt', 'r')
appendix = file.readlines()
for item in appendix:
    text = item.split('\t')
    if len(text) < 2:
        break
    level = text.count('')
    if level == 0:
        ls[level].append(pdf_out.addBookmark(''.join(text[level:len(text)-1]), int(text[len(text)-1].strip()) + offset, parent= None))
    else:
        ls[level].append(pdf_out.addBookmark(''.join(text[level:len(text)-1]), int(text[len(text)-1].strip()) + offset, parent= ls[level-1][len(ls[level-1])-1]))

# 将输出结果进行保存
with open(r'chulihou/概率论解析.pdf', 'wb') as fout:
    pdf_out.write(fout)
    