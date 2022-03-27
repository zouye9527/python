from tkinter import *
root = Tk()
v1 = IntVar()            #用来表示按钮是否选中
v2 = IntVar()
c1 = Checkbutton(root,text='python',variable=v1)
c2 = Checkbutton(root,text='java',variable=v2)
c1.pack()
c2.pack()
mainloop()

