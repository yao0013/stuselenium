import requests
import re

url = "https://www.qiushibaike.com/text/"

resq = requests.get(url=url)

html = resq.text

names = re.findall('<h2>(.*?)</h2>',html,re.S)

for name in names:
    print(name)