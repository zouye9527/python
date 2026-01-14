# 小明需要编写一个程序来统计一段文本中各个字符出现的次数。
# 程序能够接收用户输入的一段文本
# 统计每个字符出现的次数（不区分大小写）
# 输出每个字符及其出现次数
def count_characters(text):
    text = text.lower()
    char_count = {}
    # 遍历文本中的每个字符
    for char in ①:
        if char.isalnum():  # 如果是字母或数字，进行统计
            if ② in char_count:
                char_count[char]+=1
            else:
                char_count[char]=③
    return char_count
# 主程序
text = input("请输入一段文本：")
result = ④(text)
# 输出结果
print("字符出现次数统计：")
for char, count in result.items():
    print(f"'{char}': {count}次")
# 补充代码中的缺失部分，完成字符统计功能。
# 请填写缺失的代码： ①               ②             	③             	④             
