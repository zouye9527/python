#导入tk
import tkinter as tk
#创建tk窗口
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

var = tk.StringVar()
l = tk.Label(window, bg='yellow', width=40, height=2,text='请选择你想要的功能：')

#触发功能即按下按钮后想要程序做什么
def print_selection():
    l.config(text='正在为你加载 ' + var.get()+"... ...")
 
#按钮1及其功能
r1 = tk.Radiobutton(window, text='成绩查询' ,variable=var, value='成绩查询',command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text='信息查询',variable=var, value='信息查询',command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window, text='成绩录入',variable=var, value='成绩录入',command=print_selection)
r3.pack()

