import random
import re
from collections import Counter

import time
from pytagcloud import create_tag_image, make_tags, LAYOUT_HORIZONTAL
from pytagcloud.colors import COLOR_SCHEMES
from pytagcloud.lang.counter import get_tag_counts


# 去除内容中的非法字符 (Windows)
def validatecontent(content):
    # '/\:*?"<>|'
    rstr = r"[\/\\\:\*\?\"\<\>\|\.\*\+\-\(\)\"\'\（\）\！\？\“\”\,\。\；\：\{\}\{\}\=\%\*\~\·]"
    new_content = re.sub(rstr, "", content)
    return new_content


language = 'MicrosoftYaHei'
imglength = 400
imgwidth = 300
file = open('comm.txt', 'r')
data = file.read().split('\r\n')
arr = []
for content in data:
    contents = validatecontent(content).split()
    for word in contents:
        arr.append(word)
counts = Counter(arr).items()
# 用一个时间来命名
nowtime = time.strftime('%Y%H%M%S', time.localtime())
# 设置字体大小
fontsz = 120
tags = make_tags(counts, maxsize=int(fontsz))

create_tag_image(tags, 'cloud_large.png', size=(imglength, imgwidth), fontname=language,background=(0, 0, 0, 255),layout=LAYOUT_HORIZONTAL,)
