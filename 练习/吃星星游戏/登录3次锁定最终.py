import tkinter as tk
from tkinter import messagebox

def check_credentials(event=None):
    global attempts
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "123456":
        messagebox.showinfo("登录成功", "用户名和密码正确！")
        root.destroy()
    else:
        attempts += 1
        if attempts >= 3:
            messagebox.showwarning("账户锁定", "用户名或密码输入错误超过3次，账户已锁定！")
            root.destroy()
        else:
            messagebox.showerror("登录失败", f"用户名或密码错误！您还有{3-attempts}次机会。")
            entry_username.delete(0, tk.END)
            entry_password.delete(0, tk.END)

# 创建主窗口
root = tk.Tk()
root.title("登录验证")
root.geometry("400x300")  # 设置窗口大小
root.resizable(False, False)  # 禁止调整窗口大小

# 居中窗口
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height/2 - window_height/2)
position_right = int(screen_width/2 - window_width/2)
root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

# 添加标签和输入框
label_username = tk.Label(root, text="请输入用户名：", font=('Arial', 12))
label_username.pack(pady=10)

entry_username = tk.Entry(root, font=('Arial', 12))
entry_username.pack(pady=10)

label_password = tk.Label(root, text="请输入密码：", font=('Arial', 12))
label_password.pack(pady=10)

entry_password = tk.Entry(root, show="*", font=('Arial', 12))
entry_password.pack(pady=10)

# 添加按钮
button = tk.Button(root, text="登录", command=check_credentials, font=('Arial', 12))
button.pack(pady=20)

# 绑定回车键到登录按钮
root.bind('<Return>', check_credentials)

attempts = 0

root.mainloop()
