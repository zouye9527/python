# 寻找10000以内满足a+b=a*b且a≠b≠0的所有数对

results = []  # 用于存储所有满足条件的数对

for a in range(1, 1000000):  # a从1开始，因为a≠0
    for b in range(1, 10000):  # b从1开始，因为b≠0
        if a != b and a + b == a * b:  # 检查a≠b和a+b=a*b
            results.append((a, b))

# 打印所有找到的数对
for result in results:
    print(f"(a, b) = ({result[0]}, {result[1]})")
