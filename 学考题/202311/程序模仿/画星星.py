'''
下图a中的Python程序运行后,会得到图b所示的结果。
分析模仿图a中的Python程序,在图c所示Python程序中的①、②、③处分别填写什么,可以得到图d所示的结果()
            ***
            ***
            ***
            图b
            @@@@@
            @@@@@
            @@@@@
            @@@@@
            图d

'''
#图a
for i in range(3):
    for j in range(3):
        print('*',end='')
    print()

#图c
for i in range(4):          #①
    for j in range(5):      #②
        print('@',end='')   #③
    print()