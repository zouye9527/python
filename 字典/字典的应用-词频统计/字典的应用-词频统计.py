# 打开“三国演义.txt”文件，读取文件内容
import jieba

# 打开文件并读取内容
f = open("三国演义.txt", "r", encoding="utf-8")
txt = f.read()
f.close() # 关闭已打开的文件，释放系统资源。

# 分词处理，存放到列表中
words = jieba.lcut(txt)

# 统计词语出现次数
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

# 转换为列表并排序
items = list(counts.items())   # 把字典中的键值对，转换为元组，存放到列表中
for i in items[:20]:
    print(i)
items.sort(key=lambda x: x[1], reverse=True)  # 按元组中的第二个元素，逆序（降序）排列

# 输出前20个词语
for i in range(20):
    print(items[i][0],items[i][1])