#打开“三国演义.txt”文件，读取文件内容
import jieba                                    #导入jieba分词
f = open("三国演义.txt", "r", encoding='utf-8')   #打开文件
txt = f.read()                                  #读取文件内容

#分词
words = jieba.lcut(txt)                        #将句子拆分为词语保存到列表中

#统计
counts = {}                                     #建立空字典，用于存储词和出现次数
for word in words: 
    if len(word) == 1:                          #单字的词语忽略不计
        continue
    else:
        counts[word] = counts.get(word,0) + 1   #出现次数+1

#排序
items = list(counts.items())                    #字典转化为列表后才可以排序
items.sort(key = lambda x:x[1], reverse = True) #对列表items按“次数”降序排序

#输出前20个元素的值
for i in range(20): 
    print (items[i][0], items[i][1])

