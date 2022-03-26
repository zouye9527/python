import tkinter
from tkinter import simpledialog
root=tkinter.Tk()
dlg= tkinter.simpledialog.SimpleDialog(root,
                          text = 'hello SimpleDialog',
                          buttons = ['是','No','cancel','第四个','第五个']
                          )
print(dlg.go())
root.mainloop()
