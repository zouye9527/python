from re import T
from tkinter import *
root = Tk()

product = ['matebook','无线耳机','蓝牙鼠标','鼠标垫','双肩包']
v = []
for i in product:
    v.append(IntVar()) #这里注意 IntVar()
    b = Checkbutton(root,text=product,variable=v[-1],onvalue='T',offvalue='F')  #这里注意 variable[-1]
    b.pack(anchor=W)# 这个是左对齐
for i in range[5]:
    if v[0]=='T':
        pay=2000+

mainloop()

