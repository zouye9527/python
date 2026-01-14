# 学校举行数学竞赛，需要统计学生的成绩。编写一个Python程序，
# 输入一组学生成绩（整数），输入-1表示输入结束，计算并输出平均成绩、最高分和最低分。
scores = []
while True:
    score = int(input("请输入成绩（输入-1结束）："))
    if score==-1:  # ①
        break
    scores.append(score)    # ②
if len(scores) > 0:
    avg = sum(scores) / len(scores)   # ③
    max_score = max(scores)
    min_score = min(scores)  # ④
    print(f"平均成绩：{avg:.2f}")
    print(f"最高分：{max_score}")
    print(f"最低分：{min_score}")
else:
    print("未输入成绩")
# 请填写缺失的代码： ①               ②             	③             	④