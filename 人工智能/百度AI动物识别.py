from aip import *  # pip install baidu_aip


APP_ID='23942564'
API_KEY='7uL42GlUO4mMYnVGxUp8GU8i'
SECRET_KEY='5CxKfUO9412hbTueg9NMwajx82M3op52'

client=AipImageClassify(APP_ID,API_KEY,SECRET_KEY)
def get_file_content(filePath):
	with open(filePath,'rb') as fp:
		return fp.read()

image=get_file_content('0.jpg')
result=client.animalDetect(image)['result']
for i in result:
	print(i['name'],i['score'])