'''
输入身高，体重计算bmi，并判定等级
'''
import tkinter
import tkinter.messagebox
 
root = tkinter.Tk()
root.title('BMI计算3.0')
root.geometry('250x160')

bmi = tkinter.StringVar()

label = tkinter.Label(root,text='BMI计算')
label.place(x=80,y=10,height=30,width=80)

labelWeight = tkinter.Label(root,text='体重（kg）')
labelWeight.place(x=20,y=40,height=20,width=80)

labelHeight = tkinter.Label(root,text='身高（m）')
labelHeight.place(x=20,y=80,height=20,width=80)

weight = tkinter.StringVar(root)
entryWeight = tkinter.Entry(root,width=150,textvariable=weight)
entryWeight.place(x=90,y=40,height=20,width=80)

height = tkinter.StringVar(root)
entryHeight = tkinter.Entry(root,width=150,textvariable=height)
entryHeight.place(x=90,y=80,height=20,width=80)


def msgbox():
    bmi.set = round(float(entryWeight.get())/(float(entryHeight.get())*float(entryHeight.get())),2)
    if bmi.set<18.5:                             
        tkinter.messagebox.showinfo(title='BMI计算结果', message='你的BMI指数是 {result} 低体重'.format(result=bmi.set))
    elif bmi.set<23.9:
        tkinter.messagebox.showinfo(title='BMI计算结果', message='你的BMI指数是 {result} 正常'.format(result=bmi.set))
    elif bmi.set<30:
        tkinter.messagebox.showinfo(title='BMI计算结果', message='你的BMI指数是 {result} 超重'.format(result=bmi.set))
    else :
        tkinter.messagebox.showinfo(title='BMI计算结果', message='你的BMI指数是 {result} 肥胖'.format(result=bmi.set))
    return 
        
button = tkinter.Button(root,text='计算BMI',command=msgbox)
button.place(x=80,y=110,height=30,width=80)

root.mainloop()

