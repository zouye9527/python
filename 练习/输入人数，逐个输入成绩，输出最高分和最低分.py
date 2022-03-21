"""
输入人数，逐个输入成绩，输出最高分和最低分
"""
m=int(input("请输入人数："))
d=[]
for i in range(m):
    d.append(int(input("请分别输入成绩%d :"%(i+1)))) # 自己查查这句话吧，我也是找的
print("成绩列表为：",d)
print("最高分：",max(d))
print("最低分：",min(d))
