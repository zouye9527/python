import requests   #引入Python模块
import json

form = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": ""
        }
    },
    "userInfo": {  
        "apiKey": "_____________________________",# 这里填入apiKey
        "userId": "123456"  
    }
}

while True:
    # 自动询问“您想了解点什么呢？”
    form.get('perception').get('inputText')['text'] = input("您想了解点什么呢？\n")
    
    # 向“图灵机器人”官网发出请求
    #向网络服务发送请求，具体服务器地址为：http://openapi.tuling123.com/openapi/api/v2
    res = requests.post('______________________________', data=json.dumps(form))  
    result = json.loads(res.text)
    
    # 从结果中中获取最终的回复文本
    texts = result.get('results')
    for text in texts:
        if text.get('resultType') == 'text':
            print(text.get('values').get('text'))
