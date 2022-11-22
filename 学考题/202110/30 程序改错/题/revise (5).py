"""
脱氧核糖核酸（DNA）由两条互补的碱基链以双螺旋的方式结合而成。在对应位置上，
腺瞟呤（A）总是和胸腺嘧啶（T）配对，鸟嘌呤（G）总是和胞嘧啶（C）配对。输入一条单链上的碱基序列，
输出对应的互补链上的碱基序列。
输入输出样例：
输入：
ATATGGATGGTGTTTGGCTCTG
输出：
TATACCTACCACAAACCGAGAC
"""
s=input()
s1=[]

for i in range(0,len(s)+1):
    if s[i]=='A':
        s1.append('T')
    if s[i]=='T':
        s1.append('A')
    if s[i]=='G':
        s1.append('C')
    if s[i]=='C':
        s1.append('G')
for i in range(0,len(s1)+1):
    print(s1[i],end='')
    
