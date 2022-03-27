
pricedict={'1.matebook13s:2000':2000,'2.无线耳机:150':150,'3.蓝牙鼠标:30':30,'4.鼠标垫:10':10,'5.双肩包:80':80}
for i in pricedict:
    print(i)
pricenmls=list(pricedict.keys())
pricels=list(pricedict.values())
while True:
    pay1=0
    pay=0
    cart0=input('请输入要购买的商品，输入序号即可，商品之间用空格隔开：')
    cart=list(map(int,cart0.split()))
    print('您选择的商品如下：')
    for i in cart:
        print(pricenmls[i-1])
    if cart[0]==1:
        for i in cart:
            pay1=pay1+pricels[i-1]
        pay=pricels[0]*0.05+pay1*0.95
        print('应付款项为：%.2f'%pay)
        break
    else:
        x=input('必须购买matebook13s，配件才会享受九五折优惠。重新选择按y，原价购买配件按n，y/n：')
        if x=='y':
            continue
        elif x=='n':
            for i in cart:
                pay=pay+pricels[i-1]
            print('应付款为：%.2f'%pay)
