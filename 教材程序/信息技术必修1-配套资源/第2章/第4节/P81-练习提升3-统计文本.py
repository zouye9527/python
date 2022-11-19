str = input('请输入一行字符，可以是任意字符：')
count_en = count_dg = count_zh = count_pu = 0
for s in str:
    # 英文
    if "A" <= s <= "Z" or "a" <= s <= "z":
        count_en += 1
    # 数字
    elif "0" <= s <= "9":
        count_dg += 1
    # 中文
    elif u'\u4e00' <= s <= u'\u9fff':
        count_zh += 1
    # 特殊字符
    else:
        count_pu += 1
print('英文字符：', count_en)
print('数字：', count_dg)
print('中文：', count_zh)
print('特殊字符：', count_pu)

