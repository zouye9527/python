count = 0                                  # 用于记录用户错误次数
while count < 3:
    user = input("请输入您的账号：")
    pwd = input("请输入您的密码：")
    if user == 'admin' and pwd == '123':    # 进行账号密码比对
        print('登录成功')
        break
    else:
        print("用户名或密码错误")
        count += 1                            # 初始变量值自增1
        if count == 3:                       # 如果错误次数达到3次，则提示并退出
            print("输入错误次数过多，请稍后再试")
        else:
            print(f"您还有{3-count}次机会")     # 显示剩余次数
input("按回车键退出")
