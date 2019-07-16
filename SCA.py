import requests
import re

url = "http://www.maoyan.com/board/7"

resq = requests.get(url=url)

html = resq.text

names = re.findall('<p class="name"><a.*?title="(.*?)"',html,re.S)

actors = re.findall('<p class="star">(.*?)</p>',html,re.S)

times = re.findall('<p class="releasetime">(.*?)</p>',html,re.S)

scores = re.findall('<p class="score"><i class="integer">([0-9]\.)</i><i class="fraction">([0-9])</i>',html,re.S)


for name in names:
    print(name)

for actor in actors:
    print(actor.strip())

for time in times:
    print(time)

for score in scores:
    print(score)
