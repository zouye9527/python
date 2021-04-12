import pandas as pd
df=pd.read_csv("data.csv",encoding="gb2312",header=0)
quanguo=2074.53
for index,row in df.head().iterrows():
   res=row["2017年人均水资源量"]/quanguo
   res_per="{:.2%}".format(res)
   df.loc[index,"所占比重"]=res_per
print(df[["2017年人均水资源量","所占比重"]])
df.to_csv("xindata.csv",encoding="gb2312",float_format="%.2f")
