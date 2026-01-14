# 在线购物平台需要验证用户密码的强度。
# 密码强度规则：长度至少8位，包含大写字母、小写字母和数字。
# 编写一个Python程序，检查密码是否符合强度要求。
def check_password(password):
    if len(password)< 8:   # ①
        return False
    # 检查是否包含大写字母、小写字母和数字
    has_upper = False
    has_lower = False
    has_digit = False
    for char in password:  # ②
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True    # ③
    
    return has_upper and has_lower and has_digit
# 主程序
password = input("请输入密码：")
if check_password(password): # ④
    print("密码强度符合要求")
else:
    print("密码强度不符合要求")
# 请填写缺失的代码： ①               ②             	③             	④             