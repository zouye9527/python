'''
打开素材文件夹中的python＼test3．py，在该文件中完成程序。已知24小时PM2.5平均值和空气质量状况的对应关系为：
1、空气污染指数为0—50（含），空气质量状况属于优。
2、空气污染指数为51—100（含），空气质量状况属于良。
3、空气污染指数为101—150（含），空气质量状况属于轻度污染。
4、空气污染指数为151—200（含），空气质量状况属于中度污染。
5、空气污染指数为201—300（含），空气质量状况属于重度污染。
6、空气污染指数大于300，空气质量状况属于严重污染。
小王要对输入的某些城市PM2.5的情况，根据上面的对应关系，输出空气质量，输入-1表示数据输入结束
输入
7 
衢州 12 
玉树 16 
宁波 17 
喀什 500 
海南 432 
黄南 189 
兰州 127
注：输入数据包括n＋1行（n<=30）第一行中的数n表示接下来会输入n个城市的数据，接下里的n行中的每一行包括城市名称和PM2.5的数据，中间以空格分隔
输出 
衢州 优 
玉树 优 
宁波 优 
喀什 严重污染 
海南 严重污染 
黄南 中度污染
兰州 轻度污染

注：输出的n行数据中的每一行包括两部分信息，
第一部分为城市名称，第二部分为空气质量，中间以空格分隔
'''
n=int(input())
s1=[]
s2=[]
s3=[]
for i in range(n):
    s0=input().split()
    s1.append(s0[0])
    s2.append(int(s0[1]))
for i in range(n):
    if 0<s2[i]<=50:
        s3.append("优")
    elif s2[i]<=100:
        s3.append("良")
    elif s2[i]<=150:
        s3.append("轻度污染")
    elif s2[i]<=200:
        s3.append("中度污染")
    elif s2[i]<=300:
        s3.append("重度污染")
    else:
        s3.append("严重污染")
for i in range(n):
    print(s1[i],s3[i])