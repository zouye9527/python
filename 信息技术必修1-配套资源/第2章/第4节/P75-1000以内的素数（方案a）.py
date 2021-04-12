k = True
for n in range(2, 1000):
    if n == 2:
        print(n)
    m = n // 2
    if n % 2 != 0:
        for j in range(2, m + 1):
            if n % j == 0:
                k = False
                break
        if k :
            print(n)
    k = True

