import tkinter as tk
from tkinter import simpledialog
root=tk.Tk()
r = simpledialog.askstring('字符录入', '请输入字符', initialvalue='hello world!')
root.mainloop()
