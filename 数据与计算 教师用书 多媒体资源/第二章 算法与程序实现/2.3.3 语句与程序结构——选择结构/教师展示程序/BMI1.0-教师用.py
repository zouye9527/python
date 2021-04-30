from tkinter import *

root=Tk()
   
    
root.title("BMI测定1.0")
Label(root,text="您的身高(m)").grid(row=0)

Label(root,text="您的体重(kg)").grid(row=1)


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
    
    e1.delete(0,END)
    e2.delete(0,END)

Button(root,text="计算BMI值",width=10,command=show).grid(row=3,column=1,sticky=W,padx=10,pady=5)

mainloop()
