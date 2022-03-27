'''
商场商品打折促销，满3件三折，否则六折，会员再打九五折
依次输入商品价格，判断是否是会员
输出应付款，保留2位小数
'''
n=0
s=0
while True:
	a=float(input('请输入第%d件商品价格,输入0中止：'%(n+1)))
	if a==0:
		break
	s=s+a
	n+=1
if n>=3:
	pay=s*0.3
else:
	pay=s*0.6
memno='8017'
memif=input('请输入会员电话后四位')
if memif==memno:
	pay=pay*0.95
	print('会员您好，应付款为：%.2f'%pay)
else:
	print('您不是会员，应付款为：%.2f'%pay)
