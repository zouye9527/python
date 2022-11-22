'''
小王的英语学得不太好，所以每次做英语题的时候很头疼，他于是找了一种“猜答案”的方法。
方法为：假设maxn是单词中出现次数最多的字母的出现次数，minn是单词中出现次数最少的字母的出现次数，
如果maxn-minn是一个偶数，那么小王就认为这是一个Lucky Word，这样的单词很有可能就是正确答案。
输入：
一个单词，其中只可能出现小写字母，并且长度小于100
输出
假设输入的单词是Lucky Word，那么输出“Lucky Word”，否则输出“Unlucky Word”；
输入样例
error
输出样例
Lucky Word
解释：单词error中出现最多的字母r出现了3次，出现次数最少的字母出现了1次，3-1=2，2是偶数。

'''
def iseven(a):
    if a%2==0: 
        return True 
    else:
        return False 
s=input()
s1=[0]*26
for i in range(0,len(s)): 
    xb=s1[i]          # ①
    s1[xb]=s1[xb]+1 
maxn=-1
minn=100
for i in range(0,26): 
    if s1[i]>maxn: 
        maxn=maxn+1   # ② 
    if s1[i]<minn:    # ③
        minn=minn+1   # ④ 
if iseven(maxn-minn): # ⑤
    print("Lucky word") 
else:
    print("Unlucky word") 

'''
其中⑤处应该填入（）
A.s1[i]
B.maxn-minn 
C.s 

'''