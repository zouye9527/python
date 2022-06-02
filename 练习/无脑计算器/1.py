import tkinter
import tkinter.messagebox
from datetime import datetime

root = tkinter.Tk()
root.title('年龄计算器')
root.geometry('200x150')

sw = root.winfo_screenwidth()
#得到屏幕宽度

sh = root.winfo_screenheight()
#得到屏幕高度

ww = 200
wh = 150
#窗口宽高为100

x = (sw-ww) / 2
y = (sh-wh) / 2

root.geometry("%dx%d+%d+%d" %(ww,wh,x,y))

label = tkinter.Label(root,text='年龄计算器')
label.place(x=50,y=10,height=20,width=80)

labelAge = tkinter.Label(root,text='出生年份')
labelAge.place(x=5,y=50,height=20,width=80)

age = tkinter.StringVar(root)
entryAge = tkinter.Entry(root,width=150,textvariable=age)
entryAge.place(x=70,y=50,height=20,width=80)

def nl():
    nl1 = datetime.now().year-int(entryAge.get())
    tkinter.messagebox.showinfo(title='年龄计算器', message='你的年龄是 {result} '.format(result=nl1)) 
    return 
        
button = tkinter.Button(root,text='计算年龄',command=nl)
button.place(x=50,y=90,height=30,width=80)

root.mainloop()

