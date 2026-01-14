fruit={
    "apple":"苹果",
    "banana":"香蕉",
    3:"序号3"
}

# get()方法访问值
print(fruit.get("apple","这个水果不在字典里"))
print(fruit.get("pear","这个水果不在字典里"))

# 遍历字典1：遍历所有的键
for key in fruit:
    print(f"键：{key},值：{fruit[key]}")

# 遍历字典2：直接遍历键值对
for key,value in fruit.items():
    print(f'键：{key},值：{value}')

