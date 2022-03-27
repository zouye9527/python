from tkinter import *

root=Tk()

    
root.title("商品选购")

p1=2000
p2=150
p3=50
p4=10
p5=90

v1 = IntVar()            #用来表示按钮是否选中
v2 = IntVar()
v3 = IntVar()            #用来表示按钮是否选中
v4 = IntVar()
v5 = IntVar()            #用来表示按钮是否选中


c1 = Checkbutton(root,text='matebook13s:2000',variable=v1)
c2 = Checkbutton(root,text='无线耳机:150',variable=v2)
c3 = Checkbutton(root,text='蓝牙鼠标:50',variable=v3)
c4 = Checkbutton(root,text='鼠标垫:10',variable=v4)
c5 = Checkbutton(root,text='双肩包:90',variable=v5)
c1.pack()
c2.pack()
c3.pack()
c4.pack()
c5.pack()


e1=Entry(root)
e2=Entry(root)

e1.grid(row=0,column=1,padx=10,pady=5)
e2.grid(row=1,column=1,padx=10,pady=5)

def show():
    
    s=float(e1.get())
    t=float(e2.get())
    bmi=round(t/(s*s),2)
    
    Label(root,text="您的健康指数：").grid(row=4)
    Label(root,text=bmi).grid(row=4,column=1,sticky=N)
    Label(root,text="健康评价：").grid(row=5)
    
    if 23.2>bmi>16.5:
        Label(root,text="健康").grid(row=5,column=1,sticky=N)
        
        #g.msgbox("健康")
    else:
        Label(root,text="不健康").grid(row=5,column=1,sticky=N)
        #g.msgbox("不健康")
    

e1.delete(0,END)
e2.delete(0,END)
Button(root,text="计算BMI值",width=10,command=show).grid(row=3,column=1,sticky=W,padx=10,pady=5)

mainloop()
