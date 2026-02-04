# 导入jieba分词库
import jieba

# 打开文件
f=open('三国演义.txt','r',encoding='utf-8')
txt=f.read()
f.close()

# 分词，存放到列表中
words=jieba.lcut(txt)

# 统计
counts={}
for i in words:
    if len(i)==1:
        continue
    else:
        counts[i]=counts.get(i,0)+1

# 排序
ls=list(counts.items())
ls.sort(key=lambda x:x[1],reverse=True)
 
# 输出
for i in range(20):
    print(ls[i][0],ls[i][1])
