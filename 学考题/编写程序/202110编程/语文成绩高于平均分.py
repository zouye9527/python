"""
请帮助王老师统计一下小组成员的语文成绩高于平均分的学号。
输入
5
001 68
002 89
003 78
004 96
005 99
输出
86.0
002
004
005
说明：其中输入数据的第一行表明有5名同学，接下来的5行中，第一个数为学生的学号，第二个数为语文成绩，
输入顺序不一定是按照学号顺序。小组成员大于5个，小于20个。输出的第一行为平均成绩（保留一位小数），
接下来的数据是语文成绩高于平均分的学生的学号。
"""
def ave(list):
  return float(sum(list))/len(list)

n=int(input())
nu,score=[],[]
for i in range(n):
  s=input()
  nu.append(s[:3])
  score.append(float(s[3:]))
av=ave(score)
print("%.1f"%av)
for i in range(n):
  if score[i] > av:
    print(nu[i])
