while(True):
    h=float(input('请输入身高米：'))
    w=float(input('请输入体重kg：'))
    s=str(input('请输入性别：'))
    bmi=w/(h*h)
    if(s=='女'):
        if(bmi<=16.4):
            print("低体重")
        elif(bmi<=22.7):
            print("正常体重")
        elif(bmi<25.3):
            print("超重")
        else:
            print("肥胖")
    if(s=='男'):
        if(bmi<=16.4):
            print("低体重")
        elif(bmi<=23.2):
            print("正常体重")
        elif(bmi<26.4):
            print("超重")
        else:
            print("肥胖")
    isQ=input("是否要继续，继续输入“y”，退出请输入“q”：")
    if(isQ=='y'):
        continue
    elif(isQ=='q'):
        break
