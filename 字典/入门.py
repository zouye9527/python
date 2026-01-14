fruit={
    "apple":"苹果",
    "banana":"香蕉",
    "orange":"橘子"
}
print(fruit["apple"]) # 通过键找值
print(fruit["banana"])

# 通过键修改值
fruit["banana"]="香甜的香蕉"
print(fruit["banana"])

# 添加新的键值对：直接给不存在的键赋值，就可以添加
fruit["grape"]="葡萄"
print(fruit)

fruit[3]="序号3"
print(fruit)

# 获取字典所有的键keys
print(fruit.keys())

# 获取字典所有的值values
print(fruit.values())

# 检查某个键是否在字典中
print("apple" in fruit)
print("pear" in fruit)

# 获取字典的长度:返回键值对的个数
print(len(fruit))