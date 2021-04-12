k=1
for n in range(2, 1000):
    for j in range(2, n):
        if n % j == 0:
            k = 0
            break
    if k == 1:
        print(n)
    k = 1

