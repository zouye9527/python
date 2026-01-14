# 学校举行运动会，需要编写一个程序来计算高二1班的总分（为整数）
# 每个项目的得分从键盘输入中获取，最终输出高二1班的总分。
num_projects = int(input("请输入项目数量：")) # ①
s=0  # ②
for i in range(num_projects):
    print(f"请输入第{i+1}个项目的分数：")
    score = input("该项目分数是：")
    s+=int(score)   # ③
# 输出结果
print("高二1班总分：",s)    # ④
# 请填写缺失的代码： ①               ②             	③             	④             