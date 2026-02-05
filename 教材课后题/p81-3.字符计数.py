'''
编写程序，统计一段文本中分别有多少个汉字、英文字母、数字和其他字符。
'''
f=open('text.txt','r',encoding='utf-8')
text=f.read()
f.close

han =char =num =qita=0
for i in text:
    if '\u4e00' <= i <= '\u9fff':
        han+=1
    elif i.isdigit():
        num+=1
    elif i.isalpha():
        char+=1
    else:
        qita+=1
print(f'汉字{han}个，数字{num}个，字母{char}个，其他字符{qita}个')