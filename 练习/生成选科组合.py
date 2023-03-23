"""
1.输入0,输出所有组合
2.输入1,输出物理的所有组合
3.输入2,输出历史的所有组合

"""
course=["物理","历史"]
course2=["化学","生物","地理","政治"]
while True:
    print("---------------------\n1.输入0,输出所有组合\n2.输入1,输出物理的所有组合\n3.输入2,输出历史的所有组合\n4.输入n结束\n---------------------")
    t=input("请输入:")
   
    if t=='0':
        for i in course:
            for j in range(0,3):
                if j==0:
                    for k in range(1,4):
                        print(i,course2[j],course2[k])
                if j==1:
                    for l in range(2,4):
                        print(i,course2[j],course2[l])
                if j==2:
                    print(i,course2[j],course2[j+1])
    if t=='1':
        for j in range(0,3):
                if j==0:
                    for k in range(1,4):
                        print(course[0],course2[j],course2[k])
                if j==1:
                    for l in range(2,4):
                        print(course[0],course2[j],course2[l])
                if j==2:
                    print(course[0],course2[j],course2[j+1])
    if t=='2':
        for j in range(0,3):
                if j==0:
                    for k in range(1,4):
                        print(course[1],course2[j],course2[k])
                if j==1:
                    for l in range(2,4):
                        print(course[1],course2[j],course2[l])
                if j==2:
                    print(course[1],course2[j],course2[j+1])
    if t=='n':
        break
    else:
        print("输入有误，重新输入")

