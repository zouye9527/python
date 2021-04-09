# coding=utf-8# python3.7
 
 
import json
from pprint import pprint
from aip import AipOcr
 
appId = '23942800'
apiKey = 'FpGRgkjDV1tDpvNvOBGKyUkG'
secretKey = 'sVrlQMVp3i13xp0l3RgOSRFv3wzDNNFB'
 
# 请求连接服务器
client = AipOcr(appId, apiKey, secretKey)
 
# 获取本地图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
image = get_file_content(r'2.png')
 
# 设置语言，这是百度api的参数，可查看官方文档
options = {'language_type':'CHN_ENG'}
 
# 返回json格式数据
res = client.basicGeneral(image, options)
 
pprint(res)
with open('test.json', 'w') as f:
    json.dump(res,f, ensure_ascii=False, indent=4)