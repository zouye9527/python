#打开“三国演义.txt”文件，读取文件内容
import jieba                                  #导入jieba分词
excludes = {"将军","却说","荆州","二人","不可","不能","如此","商议","如何","公主","军士","主公","左右","军马","引兵","次日","大喜","天下","东吴","于是","今日","不敢","魏兵","陛下","一人","都督","人马","不知"}
f = open("三国演义.txt", "r", encoding='utf-8') #打开文件
txt = f.read()                                #读取文件内容

#分词
words = jieba.lcut(txt)                        #将句子拆分为词语保存到列表中

#统计
counts = {}                                     #建立空字典，用于存储词和出现次数
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
    counts[rword] = counts.get(rword,0) + 1
for word in excludes:
    del(counts[word])
    
#排序
items = list(counts.items())                    #字典转化为列表后才可以排序
items.sort(key = lambda x:x[1], reverse = True) #对列表items按“次数”降序排序

#输出前20个元素的值
for i in range(10): 
    print (items[i][0], items[i][1])

