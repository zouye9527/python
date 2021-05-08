#长方体(正方体)计算
print("输入长方体的长、宽、高，将进行相应的计算。长输入0，则程序结束！") 
a = 1 
while a != 0: 
    a = float(input("请输入长方体的长：")) 
    if a == 0: 
        break 
    b = float(input("请输入长方体的宽：")) 
    if b == 0: 
        print("长方体的宽不能为0，请重新输入：") 
        b = float(input()) 
    c = float(input("请输入长方体的高：")) 
    if c == 0: 
        print("长方体的高不能为0，请重新输入：") 
        c = float(input()) 
    d = 4*(a+b+c) 
    e = 2*(a*b+a*c+b*c) 
    f = a*b*c 
    print("棱长和是：",d) 
    print("表面积是：",e) 
    print("体积是：",f) 
print("程序结束！")