# "输入两个数字a和b，判断两个数字的大小关系，如果a大于b，则输出""大于"";如果a小于b，则输出""小于"";如果两个数相等，则输出""等于""。 "
# 代码中存在错误，请帮助修改。 
# 输入样例 
# 3 
# 4 
# 注:输入包括两行，第一行的数字是a，第二行的数字是b 
# 输出样例 
# 小于 
a=eval(input())
b=eval(input())
c=a-b
if c<0:
    print("小于")
elif c==0:
    print("等于")
else:
    print("大于")
