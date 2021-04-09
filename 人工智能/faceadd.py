import requests
import json
import base64
import os
from tkinter import filedialog
 
#get_token，access_token一个月更新一次，未免过期，每次都更新一次
def get_token():
    url='https://aip.baidubce.com/oauth/2.0/token'  #申请token的URL
    data={}
    data['grant_type']='23935531'         #这个必须有
    data['client_id']='auqVKL7FH8MYbN1RLyqCIo0t'    #百度该应用的APP—ID
    data['client_secret']='n2LWuIOG7v3Djk8oR7kYzlArkBt58gqg'    #相应的secret
     
    response=requests.post(url, data)
    content=response.content.decode('utf-8')
    content=json.loads(content)   
     
    #print('您的access_token为 : \r',content['access_token'])
    return content['access_token']
 
def base666(image):         #这个函数开始命名为base64，结果报错 has no attribute 'b64encode'
    f1 = open(image, 'rb')
    f1_64 = base64.b64encode(f1.read())
    f1.close()
    f1_64=f1_64.decode()
    return f1_64
 
def faceadd(face1,face2,image):
    url='https://aip.baidubce.com/rest/2.0/face/v1/merge'+"?access_token=" + get_token()
    data={"image_template":{"image":base666(face1),"image_type":'BASE64',},"image_target":{"image":base666(face2),"image_type":"BASE64",}}
    data=json.dumps(data)  
 
    headers={'Content-Type':"application/json"}
    response=requests.post(url, data,headers=headers)
    req_con1 = response.content.decode('utf-8')
     
    content=eval(req_con1)
    result = content['result']['merge_image']
    imgdata = base64.b64decode(result)
    with open(image, 'wb') as fp:
        fp.write(imgdata)
        fp.close()
     
if __name__=='__main__':
    image1 = filedialog.askopenfilename()
    image2 = filedialog.askopenfilename()
    image=os.path.dirname(image1)+'/Faceadd.jpg'
    faceadd(image1,image2,image)
