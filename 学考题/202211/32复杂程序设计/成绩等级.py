'''
已知红星学校高一物理期末考试分数和等级的对应关系：
实考分数    90-100(含)  89-80(含)   79-70(含)   69-60(含)   60以下
对应等级      A           B           C           D           E
"小王要对输入的某些同学的实考分数,根据上面的对应关系,输出对应等级。"
输入
001 95
002 85
003 74
004 63
005 32
-1
"注:输入数据包括n+1行(n<=30)前n行,每行包括同学编号和实考分数,中间以空格分隔,最后一行的-1代表输入结束"
输出
001 A
002 B
003 C
004 D
005 E
"注:输出的n行数据中的每一行包括两部分信息,第一部分为同学编号,第二部分为对应等级,中间以空格分隔"
'''
s1=[]
s2=[]
s4=[]
while True:
    s=input()
    if s[0]=="-" and s[1]=="1":
        break
    else:
        s3=s.split()
        s1.append(s3[0])
        s2.append(int(s3[1]))
for i in range(len(s2)):
    if s2[i]<60:
        s4.append("E")
    elif s2[i]<69:
        s4.append("D")
    elif s2[i]<79:
        s4.append("C")
    elif s2[i]<89:
        s4.append("B")
    elif s2[i]<=100:
        s4.append("A")
for i in range(len(s2)):
    print(s1[i],s4[i])
