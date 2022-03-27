# python常见函数

## 一、一行输入多个数据，以不同类型保存

> 例如：在一行 输入 a,b ,求a+b
>

1.以整数形式保存

```python
a,b = map(int,input().split())
print(a+b)
```

 2.输入多个数字：以浮点型形式保存：

```python
a,b,c = map(float,input().split())
```

