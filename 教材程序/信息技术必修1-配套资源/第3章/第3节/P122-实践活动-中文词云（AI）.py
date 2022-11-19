#-*- coding:utf-8 -*-

from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text = open('新一代人工智能发展规划.txt','rb').read()  # 读入  txt 文件
text_jieba = " ".join(jieba.cut(text)) # 使用 jieba 分词
bg_pic = imread('3.png')               # 读入图片

# 配置词云参数
wc = WordCloud(
    font_path = 'msyhbd.ttf', # 设置字体    
    background_color='white', # 设置背景色    
    max_words=200,            # 允许最大词汇    
    mask=bg_pic,              # 词云形状    
    max_font_size=100,        # 最大号字体
)

wc.generate(text_jieba)  # 生成词云
# 生成图片并显示
plt.figure()
plt.imshow(wc)
plt.axis('off')
plt.show()
# 保存图片
wc.to_file('AI.jpg')

