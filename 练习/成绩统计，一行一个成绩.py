'''
小张需要帮助老师统计每次考试后的最高分和最低分，请你帮助他写一个程序，第一行中输入考试同学的人数，后面各行输入每个人成绩，在一行中输出最高分和最低分。
注：输入的每个成绩不超过150分，输出结果在一行，中间以空格分隔
输入样例：
4 
98 
97 
88 
95
输出样例：
最高分 98 最低分 10
'''
cj=[]
m=1
n=int(input('请输入人数:'))
while n>0:
	score=float(input('请输入第%d个成绩:'%m))
	if score>150:
		print('输入的成绩不能超过150，重新输入')
		continue
	cj.append(score)
	m+=1
	n-=1
print('最高分是 %.2f 最低分 %.2f'%(max(cj),min(cj)))
	
