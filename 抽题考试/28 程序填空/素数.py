'''
如下的Python程序能求得[101,200]之间所有的素数，其中①、②、③处应为（ ）
'''
for i in range(101,201):   # ① 
    count=0
    for j in range(1,i+1): # ② 
        if  i%j!=0:        # ③
            count+=1 
    if count==i-2:
        print(i) 
'''
A.①101,201 ②1,i+1 ③i%j!=0 
B.①100,201 ②2,i+1 ③i%j!=0
C.①101,201 ②2,i   ③i%j==0 

'''
