'''
小刘单位发了100元购物卡，可以到联华超市购买下列洗漱用品：洗发水（15元）、洁面皂（2元）、牙膏（5元）。
若要将100元正好花掉，可有哪些购买组合？请完善程序。其中③处填写（）
A.i*15+j*5+k*2==100 and (i!=0)
B.i*15+j*5+k*2==100 and (k!=0)
C.i*2+j*5+k*15==100 and (k!=0)
'''

money=100
n=100//15         #n 洗发水最多瓶数 ①
for i in range(n,0,-1):
    m=100//5      #m 牙膏最多瓶数 ②
    for j in range(m,0,-1):
        k=(money-i*15-j*5)//2
        if i*15+j*5+k*2==100 and (k>0):    # ③
            print("洗发水有{0:2}瓶，牙膏有{1:2}瓶，洁面皂有{2:2}个".format(i,j,k))    # 4

