import subprocess

# 读取IP列表文件
def read_ip_list(file_path):
    with open(file_path, 'r') as file:
        ip_list = file.read().splitlines()
    return ip_list

# 执行ping测试并返回结果
def ping(ip):
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip], timeout=2)
        return True
    except subprocess.TimeoutExpired:
        return False
    except subprocess.CalledProcessError:
        return False

# 主程序
def main():
    file_path = 'ip_list.txt'  # IP列表文件路径
    result_file_path = 'unreachable_ips.txt'  # 保存无法ping通的IP的文件路径

    ip_list = read_ip_list(file_path)
    unreachable_ips = []

    for ip in ip_list:
        if not ping(ip):
            unreachable_ips.append(ip)

    if len(unreachable_ips) > 0:
        # 输出无法ping通的IP列表
        print("无法ping通的IP列表:")
        for ip in unreachable_ips:
            print(ip)

       
        # 保存无法ping通的IP列表到文件
        with open(result_file_path, 'w') as file:
            for ip in unreachable_ips:
                file.write(ip + '\n')
        print(f"无法ping通的IP列表已保存至文件: {result_file_path}")
    else:
        print("所有IP均可ping通。")

if __name__ == '__main__':
    main()
