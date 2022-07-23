"""
Created on 2022-7-23 18:06:53
@author: Keithen
"""

from urllib import request
from urllib.request import urlopen
import re
import pandas as pd

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
headers = {'User-Agent': user_agent}

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner#tab4'
requests = request.Request(url, headers=headers)
response = urlopen(requests, timeout=30)
# content = response.read().decode('unicode_escape')        # 由于解析网页所有内容非常耗时
content = open('caselist.txt', 'r', encoding="utf-8").read()  # 因此只提取了核心部分作为匹配内容

# 匹配模式设置
pattern = re.compile(
    '.*?"confirmed":"(.*?)".*?"died":"(.*?)".*?"crued":"(.*?)".*?"confirmedRelative":"(.*?)".*?"curConfirm":"(.*?)".*?"area":"(.*?)".*?',
    re.M)
# confirmed 累计确诊 died 死亡 crued 治愈 confirmedRelative 新增确诊 curConfirm 现有确诊
items = re.findall(pattern, content)

data = pd.DataFrame(columns=['疫情地区', '新增', '现有', '累计', '治愈', '死亡'])
cnt = 0
for i in items:
    data.loc[cnt, '疫情地区'] = i[5]
    data.loc[cnt, '现有'] = i[4]
    data.loc[cnt, '新增'] = i[3]
    data.loc[cnt, '累计'] = i[0]
    data.loc[cnt, '治愈'] = i[2]
    data.loc[cnt, '死亡'] = i[1]
    cnt += 1

print(data)
data.to_csv('新冠疫情实时数据.csv', encoding="utf-8_sig", index=False)
