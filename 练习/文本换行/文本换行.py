import re

# 读取原始文件
with open("D:\\GitHub\\练习\\文本换行\\1.txt", "r", encoding="utf-8") as file:
    content = file.read()

# 用正则表达式在每行第一个汉字前插入一个换行符
content = re.sub(r"^([\S\s]*?)([\u4E00-\u9FA5]+)", r"\1\n\2", content, flags=re.MULTILINE)

# 将处理后的文件保存
with open("D:\\GitHub\\练习\\文本换行\\new_1.txt", "w", encoding="utf-8") as file:
    file.write(content)
