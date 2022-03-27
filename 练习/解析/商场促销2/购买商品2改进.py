# 初始化商品数据
pricenmls=['1.matebook13s:2000','2.无线耳机:150','3.蓝牙鼠标:30','4.鼠标垫:10','5.双肩包:80']
pricels=[2000,150,30,10,80]
# 输出商品价格表
for i in pricenmls:
    print(i)
# 开始计算
while True:
    pay1=0
    pay=0
    # 输入要购买的商品序号
    cart0=input('请输入要购买的商品，输入序号即可，商品之间用空格隔开：')
    cart=list(map(int,cart0.split())) # 购物车字符串转为数字列表
    
    members=input('是会员吗？是y,否n：') # 是否会员

    # 打印出选择的商品清单
    print('您选择的商品如下：')
    existif=0 # 标记出商品清单中是否选择了matebook
    for i in cart:
        print(pricenmls[i-1])
        if i==1:
            existif=1
    # 如果是会员   
    if members=='y':
        if existif==1:
            for i in cart:
                pay1=pay1+pricels[i-1] #从价格列表中按（商品序号-1）查找商品价格，累加，赋值给pay1
            pay=(pricels[0]*0.1+pay1*0.9)*0.95 #按优惠价*会员折扣：求和，并乘以会员折扣
            print('应付款项为：%.2f'%pay)
            break
        else:
            x=input('必须购买matebook13s，配件才会享受九折优惠。重新选择按y，原价购买配件按n，y/n：')
            if x=='y':
                continue 
            elif x=='n':
                for i in cart:
                    pay=pay+pricels[i-1]
                pay=pay*0.95 #会员折扣
                print('应付款为：%.2f'%pay)
            break
    # 如果不是会员
    elif members=='n':
        if existif==1:
            for i in cart:
                pay1=pay1+pricels[i-1] #从价格列表中按（商品序号-1）查找商品价格，累加，赋值给pay1
            pay=pricels[0]*0.1+pay1*0.9 #优惠折扣
            print('应付款项为：%.2f'%pay)
            break
        else:
            x=input('必须购买matebook13s，配件才会享受九五折优惠。重新选择按y，原价购买配件按n，y/n：')
            if x=='y':
                continue
            elif x=='n':
                for i in cart:
                    pay=pay+pricels[i-1] #无折扣
                print('应付款为：%.2f'%pay)
            break