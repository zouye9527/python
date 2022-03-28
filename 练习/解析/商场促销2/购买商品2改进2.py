a=int(input('请输入MateBook 13s的价格a：'))
n1=int(input('MateBook 13s购买数量n1：'))
b=int(input('配件价格b：'))
n2=int(input('配件购买数量n2：'))
if n1>0:
    pay=a*n1+b*n2*0.9
else:
    pay=b*n2
print('%.2f'%pay)