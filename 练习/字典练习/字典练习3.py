cj={}
while True:
    s=input()
    if s[0]=='-' and s[1]=='1':
        break
    else:
        s1=s.split()
        cj[s1[0]]=int(s1[1])
print(cj)

