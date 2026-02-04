# 打开“三国演义.txt”文件，读取文件内容
import jieba

# 打开文件并读取内容
f = open("三国演义.txt", "r", encoding="utf-8")
txt = f.read()
f.close()

# 分词处理，存放到列表中
words = jieba.lcut(txt)

# 统计词语出现次数
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "诸葛亮" or word == "孔明曰":
        rword = "孔明"
    elif word == "关公" or word == "云长":
        rword = "关羽"
    elif word == "玄德" or word == "玄德曰":
        rword = "刘备"
    elif word == "孟德" or word == "丞相":
        rword = "曹操"
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
    

# 转换为列表并排序
items = list(counts.items())
for i in items[:20]:
    print(i)
items.sort(key=lambda x: x[1], reverse=True)

# 输出前20个词语
for i in range(20):
    print(items[i][0],items[i][1])