'''
输入姓名，年龄，身高，体重计算bmi，并判断是否正常
'''
import tkinter
import tkinter.messagebox
 
root = tkinter.Tk()
root.title('BMI计算器')
root.geometry('300x350')

bmi = tkinter.StringVar()

label = tkinter.Label(root,text='BMI判断')
label.place(x=20,y=10,height=30,width=80)

labelName = tkinter.Label(root,text='姓名')
labelName.place(x=20,y=60,height=20,width=80)

labelAge = tkinter.Label(root,text='年龄')
labelAge.place(x=20,y=110,height=20,width=80)

labelWeight = tkinter.Label(root,text='体重')
labelWeight.place(x=20,y=160,height=20,width=80)

labelHeight = tkinter.Label(root,text='身高')
labelHeight.place(x=20,y=210,height=20,width=80)

label3 = tkinter.Label(root,text='健康指数：')
label3.place(x=10,y=280,height=20,width=80)

label4 = tkinter.Label(root,text='健康评价：')
label4.place(x=10,y=310,height=20,width=80)


name = tkinter.StringVar(root)
entryName = tkinter.Entry(root,width=150,textvariable=name)
entryName.place(x=70,y=60,height=20,width=80)

age = tkinter.StringVar(root)
entryAge = tkinter.Entry(root,width=150,textvariable=age)
entryAge.place(x=70,y=110,height=20,width=80)

weight = tkinter.StringVar(root)
entryWeight = tkinter.Entry(root,width=150,textvariable=weight)
entryWeight.place(x=70,y=160,height=20,width=80)

height = tkinter.StringVar(root)
entryHeight = tkinter.Entry(root,width=150,textvariable=height)
entryHeight.place(x=70,y=210,height=20,width=80)


def msgbox():
    bmi.set = round(float(entryWeight.get())/(float(entryHeight.get())*float(entryHeight.get())),2)
    if bmi.set<18.5:                             
        tkinter.messagebox.showinfo(title='BMI计算结果', message='你的BMI指数是 {result} 低体重'.format(result=bmi.set))
    elif bmi.set<24:
        tkinter.messagebox.showinfo(title='BMI计算结果', message='你的BMI指数是 {result} 正常'.format(result=bmi.set))
    elif bmi.set<30:
        tkinter.messagebox.showinfo(title='BMI计算结果', message='你的BMI指数是 {result} 超重'.format(result=bmi.set))
    else :
        tkinter.messagebox.showinfo(title='BMI计算结果', message='你的BMI指数是 {result} 肥胖'.format(result=bmi.set))
    return 
        
button = tkinter.Button(root,text='计算BMI',command=msgbox)
button.place(x=10,y=250,height=30,width=80)

root.mainloop()

