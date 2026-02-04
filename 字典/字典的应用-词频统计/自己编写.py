import jieba

f=open("三国演义.txt",'r',encoding="utf-8")
text=f.read()
f.close()

words=jieba.lcut(text)


counts={}
for i in words:
    if len(i)==1:
        continue
    else:
        counts[i]=counts.get(i,0)+1

ls=list(counts.items())
ls.sort(key=lambda x:x[1],reverse=True)

for i in range(20):
    print(ls[i][0],ls[i][1])