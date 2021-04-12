#-*- coding: UTF-8 -*-

#导入包
import xlrd, xlwt
import time,datetime
import pandas as pd

#设置路径
file_a='a.xls'
file_b='b.xls'
listdata_a = [['时间','温度','湿度']] # 用来保存处理后的数据
listdata_b = [['时间','PM2.5']]
clearedfile_a = 'a_copy'
clearedfile_b = 'b_copy'

def clear_data(file,listdata,clrfile):    #清洗数据并保存为excel文件
    #打开数据文件
    data=xlrd.open_workbook(file) 
    table=data.sheet_by_name(u'Sensor Data') #通过名称获得工作表
    nrows=table.nrows   #通过工作表的属性获得行数
    #清洗多余数据
    for rownum in range(1,nrows):  #用一个循环来遍历一次文件
        rowdata_bf = table.row_values(rownum-1) # 当前行前一行数据
        rowdata_nw = table.row_values(rownum)   # 当前行数据
        hour_nw = (rowdata_nw[0])[11:13]        # 取当前行时间的小时
        new_time_nw = (rowdata_nw[0])[0:13]+":00:00"  # 构造新的整点时间数据,当前行
        if ((rowdata_bf[0])[0:19] <= new_time_nw <= (rowdata_nw[0])[0:19]):  #判断整点并计算整点数据，保存至列表
            if (clrfile == 'a_copy'):
                new_rowdate = [new_time_nw,round((rowdata_bf[1]+rowdata_nw[1])/2,1),round((rowdata_bf[2]+rowdata_nw[2])/2,1)]
            if (clrfile == 'b_copy'):
                new_rowdate = [new_time_nw,round((rowdata_bf[1]+rowdata_nw[1])/2,1)]
            listdata.append(new_rowdate)
    # 保存文件
    f = xlwt.Workbook() #创建工作簿
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    for i in range(len(listdata)):
        for j in range(len(listdata[i])):
            sheet1.write(i,j,(listdata[i])[j])
    f.save(clrfile+'.xls')#保存文件

clear_data(file_a,listdata_a,clearedfile_a)
clear_data(file_b,listdata_b,clearedfile_b)

# 合并清洗后的a,b数据
df1 = pd.read_excel("a_copy.xls")
df2 = pd.read_excel("b_copy.xls")
df3 = pd.merge(df1,df2,how='outer',on='时间',sort='True')
print(df3)
df3.to_excel("MergeDates.xls",sheet_name='sheet1')






