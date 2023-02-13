# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 00:44:50 2022

@author: yuyuko

題目名稱:歷年18歲以上過重及肥胖率

csv提供機關:衛生福利部國民健康署
"""
import pandas as pd
import matplotlib.pyplot as plt
pd.set_option("display.max_rows", 1000) # 設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000) # 設定最大能顯示1000columns

df=pd.read_csv(r'File_14622.csv') # 匯入要分析的資料
print(df.pivot_table) # 顯示表格
headers = ['years','Sample Size', 'Male(%)', 'Female(%)', 'Both(%)'] # 將 columns 名稱調整成英文，方便分析操作
df.columns = headers
df.columns
print(df.pivot_table) # 顯示調整後的表格

from pylab import mpl # 指定windows默認字形：解決plot不能顯示中文問題
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei']
mpl.rcParams['axes.unicode_minus'] = False

# 轉換dataframe為csv,xlsx,html格式
df.to_csv('New_Data.csv',encoding='utf8')
df.to_excel('New_Data.xlsx',encoding='utf8')
df.to_html('New_Data.html',encoding='utf8')

#資料視覺化
#進行繪圖
plt.figure()
x = df['years']
y1 = df['Male(%)']
y2 = df['Female(%)']
y3 = df['Both(%)']
plt.title("2008~2013年歷年18歲以上過重與肥胖率")
plt.xlabel("年分")
plt.ylabel("肥胖率(%)")
plt.plot(x, y1, label='男性')
plt.plot(x, y2, label='女性')
plt.plot(x, y3, label='其他')
plt.legend(loc='lower right')
plt.savefig('plot.png')
plt.show()

# 存檔至mydatabase.db
import sqlite3
con = sqlite3.connect('mydatabase.db')
df.to_sql('users',con)