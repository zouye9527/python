ls1=[]
ls2=[]
for i in range(1,1000):
    for j in range(1,1000):
        if 5*i+1==6*j+5:
            ls1.append(i)
for k in range(1,1000):          
    for l in range(1,1000):                
        if 7*k+4==11*l+10:
            ls2.append(k)
for i in ls1:
    for j in ls2:
        if 5*i+1==7*j+4:
            print(f'一共有{5*i+1}人')
                
                   