'''
商场商品打折促销，满3件三折，否则六折
依次输入商品价格
输出应付款，保留2位小数
'''
n=0
s=0
while True:
	a=float(input('请输入第%d件商品价格,输入0中止'%(n+1)))
	if a==0:
		break
	s=s+a
	n+=1
if n>=3:
	fee=s*0.3
else:
	fee=s*0.6
print('应付款为：%.2f'%fee)
