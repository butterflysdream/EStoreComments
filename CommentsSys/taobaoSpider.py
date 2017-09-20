import http
import json
import jieba.posseg as pseg
from urllib import request,parse

import simplejson
import time


def spider(url):
    header = {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"
    };
    req = request.Request(url=url,headers=header)
    response = request.urlopen(req)
    content = response.read().decode('gbk')
    print(content)
    data = str(content)
    data = '{'+data+'}'
    print(data)
    datajson  = simplejson.loads(data)
    rateDatail = datajson["rateDetail"]
    paginator = rateDatail["paginator"]
    page = paginator['page']
    lastPage = paginator['lastPage']
    for i in range(0,lastPage):
        time.sleep(30)
        parm = {}
        parm['currentPage'] = i+1
        url_values = parse.urlencode(parm)
        full_url = url +"&"+ url_values
        print(full_url)
        req = request.Request(url=full_url, headers=header)
        response = request.urlopen(req)
        content = response.read().decode('gbk')
        data = str(content)
        data = '{' + data + '}'
        print(data)
        datajson = simplejson.loads(data)
        rateDatail = datajson["rateDetail"]
        rateList = rateDatail["rateList"]
        wordf = ['d','e','f','g','h','p','r','q']
        for rate in rateList:
            comm = rate["rateContent"]
            seg_list = pseg.cut(comm)
            with open('comm.txt', 'a') as f:
                for word, flag in seg_list:
                    if(flag not in wordf):
                        f.write(word+" ")
    # print(page)

if __name__ == "__main__":
    #itemId=534997940553&spuId=644685204&sellerId=890482188
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=534997940553&spuId=644685204&sellerId=890482188';
    spider(url);