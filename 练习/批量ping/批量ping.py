import os

# 读取文件中的IP列表
with open("E:\GitHub\python\练习\批量ping\ip_list.txt", 'r') as f:
    ip_list = f.readlines()

# 创建一个空列表来保存不能ping通的IP
unreachable_ips = []

# 遍历IP列表
for ip in ip_list:
    # 执行ping命令
    response = os.system("ping -c 1 " + ip)
    # 如果返回值不为0，说明ping不通
    if response != 0:
        unreachable_ips.append(ip)

# 输出不能ping通的IP列表
print("Unreachable IPs:")
for ip in unreachable_ips:
    print(ip)

# 将不能ping通的IP列表保存到文件中
with open('E:\GitHub\python\练习\批量ping\unreachable_ips.txt', 'w') as f:
    for ip in unreachable_ips:
        f.write(ip)
