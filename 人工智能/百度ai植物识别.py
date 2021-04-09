from aip import AipImageClassify

# 定义常量
APP_ID='23942564'
API_KEY='7uL42GlUO4mMYnVGxUp8GU8i'
SECRET_KEY='5CxKfUO9412hbTueg9NMwajx82M3op52'
# 初始化AipFace对象
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('3.jpg')
#将左侧括号内hua.jpg替换为待识别的图片路径

result=client.plantDetect(image)['result']
for i in result:
    print(i['name'],i['score'])
