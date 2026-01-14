score = []
n = 0
while True:
    a = float(input())
    if a == -1:
        break
    else:
        score.append(a)
for i in range(len(score)):
    if score[i] >= 85:
        n = n + 1
print(n)
