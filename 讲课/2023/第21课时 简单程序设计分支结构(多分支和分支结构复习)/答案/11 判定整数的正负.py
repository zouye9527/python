'''
输入一个整数，如果是正数，输出“正数”；如果是负数，输出“负数”；如果是0，输出“0”
'''
n=int(input())
if n<0:
    print("负数")
elif n==0:  #Python语言中==的书写
    print("0")
else:
    print("正数")
