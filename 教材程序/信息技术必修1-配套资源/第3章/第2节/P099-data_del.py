# 导入pandas模块并设置别名为pd
import pandas as pd
# 用pandas模块中的read_csv函数打开数据文件，指定文件的文字编码方式，指定包含列标题
df = pd.DataFrame(pd.read_csv('yongshui.csv', encoding='gb2312', header=1))
df1=df.drop_duplicates()
df1.to_csv('yongshuigai.csv', encoding='gb2312')
df2=pd.read_csv('yongshuigai.csv', encoding='gb2312')
print(df2)
