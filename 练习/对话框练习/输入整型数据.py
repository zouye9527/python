import tkinter as tk
from tkinter import simpledialog
root=tk.Tk()
r = simpledialog.askinteger('整数录入', '请输入整数', initialvalue=10)
root.mainloop()
