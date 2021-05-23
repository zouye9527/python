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
print('最高分和最低分分别是:%.2f %.2f'%(max(cj),min(cj)))
	
