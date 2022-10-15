import csv  
with open('test.csv','w+') as myFile:      
    exampleFile = open('test.csv')              # 打开csv文件
    exampleReader = csv.reader(exampleFile)     # 读取csv文件
    exampleData = list(exampleReader)           # csv数据转换为列表
    length_zu = len(exampleData)                # 得到数据行数
    length_yuan = len(exampleData[0])           # 得到每行长度
