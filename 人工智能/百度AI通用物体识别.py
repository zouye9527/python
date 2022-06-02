from aip import AipImageClassify
import tkinter as tk
from tkinter import filedialog


""" 你的 APPID AK SK """
APP_ID='23942564'
API_KEY='7uL42GlUO4mMYnVGxUp8GU8i'
SECRET_KEY='5CxKfUO9412hbTueg9NMwajx82M3op52'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
filepath = "D:\\0\\1.JPG"
filepath = filedialog.askopenfilename()
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content(filepath)

""" 调用通用物体识别 """
result=client.advancedGeneral(image);
# print(result)

result=client.advancedGeneral(image)['result']
for i in result:
    print(i['keyword'],i['root'])
