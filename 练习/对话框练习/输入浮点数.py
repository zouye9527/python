import tkinter as tk
from tkinter import simpledialog
root=tk.Tk()
r = simpledialog.askfloat('浮点数录入', '请输入浮点数', initialvalue=1.1)
root.mainloop()
