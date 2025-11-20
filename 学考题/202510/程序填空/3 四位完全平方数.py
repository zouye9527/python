for n in range(100):
    sq=n*n
    if sq>999 and sq<10000:
        s=str(sq)
        if s[0]==s[1] and s[2]==s[3]:
            if s[0]!=s[2]:
                print(sq)