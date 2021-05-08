
#单据污损
print("符合条件的数据有：")
for i in range(10):
    for j in range(10):
        a = 140901+1000*i+10*j
        if a%77 == 0:
            print (a)