k = 21
while not ((k % 5 == 1) and (k % 6 == 5) and (k % 7 == 4) and (k % 11 == 10)):
    k = k + 1
print("总人数：", k)

