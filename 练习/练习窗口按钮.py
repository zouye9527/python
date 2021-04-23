# 添加输入框
import tkinter as tk
from tkinter import *

win1=tk.Tk()
win1.title('计算BMI')#添加窗体名称
# win1.geometry('200x200')#设置窗体大小

Label(win1, text="身高（m）").grid(row=0,column=0)
Label(win1, text="体重（kg）").grid(row=1,column=0)

e1=Entry(win1)
e2=Entry(win1)

e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)

def show():
    print('身高：%s米'%e1.get())
    print('体重：%skg'%e2.get())

Button(win1,text='获取信息',width=10,command=show)\
    .grid(row=3,column=0,padx=10,pady=5,sticky=W) # sticky=W:获取信息按钮左对齐
Button(win1,text='退出',width=10,command=win1.quit)\
    .grid(row=3,column=1,padx=10,pady=5,sticky=E) # sticky=E:获取信息按钮右对齐


win1.mainloop()

