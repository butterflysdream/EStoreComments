import http
import json
import jieba.posseg as pseg
from urllib import request,parse

import re
from bs4 import BeautifulSoup
import simplejson
import time


def spider(url):
    base_url = 'https://rate.tmall.com/list_detail_rate.htm?'
    result = {}
    itemid = ""
    pat = r'https://detail.tmall.com/item.htm[?]id=[0-9]+'
    reg =  re.compile(pattern=pat)
    if(re.match(reg,url)):
        itemid = re.findall(re.compile('[0-9]+'),url)[0]
        result["product"] = get_product_info(url,itemid)
        parm = {}
        parm['sellerId'] = result["product"]["sellerid"]
        parm['itemId'] = itemid
        url_values = parse.urlencode(parm)
        full_url = base_url + "&" + url_values
        print(full_url)
        result["comms"] = get_comm(full_url)
    else:
        result['error'] = 'Please enter the correct URL!!'
    return result


if __name__ == "__main__":
    #itemId=534997940553&spuId=644685204&sellerId=890482188
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=534997940553&spuId=644685204&sellerId=890482188';
    spider(url);

def get_product_info(url,itemid):
    product = {}
    header = {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Accept - encoding": "gzip, deflate, br",
        "Cookie": "uss=WvcTf%2Fm0FVNmFsJTmyzfORO5c5j7e%2ByfWEBy4a%2FlVsc9fGhbZBLCzdGTPg%3D%3D; _m_h5_tk=02350c868a5edde2bc970cac800368c6_1505893868202; _m_h5_tk_enc=33952373d6576df9977c52b9e9bbccb1; cna=6ddIElTq+hQCAXFshQLlWDhg; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; isg=Avj4F8WQ1ZlDFjl5a5uLEG-HyaZKyVVV7xLuCDJq_zOUTYg32nNce8stc3OG; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTcCfOicyCJkg%3D%3D; uc3=sg2=AVH%2FkEb8%2Bgdy3jLSerMFMambpOr2BLqt5zmUjIVupTs%3D&nk2=AQuN88GK&id2=VAMVeCmJEWbD&vt3=F8dBzWjJcyKPrrWrO5c%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; t=dcf7cbf1344fe32442371f734409967a; tracknick=bonehj; lgc=bonehj; _tb_token_=563ae5137ef55; cookie2=3f19758d9dc2fae097b909005a7262ea"
    }
    req = request.Request(url=url, headers=header)
    response = request.urlopen(req)
    content = response.read().decode('gbk')
    soup = BeautifulSoup(content, "html.parser")
    item = soup.find(id='dsr-userid')
    product["sellerid"] = item["value"]
    item2 = soup.find(id='J_AttrUL')
    title = [title["title"] for title in item2.find_all('li')]
    product["p_name"] = title[0]
    product["brand"] = title[4]
    product["price"] = title[6]
    product["imgurl"] = soup.find(id="J_ImgBooth")["src"]
    product["url"] = url
    product["itemid"] = itemid
    return product

def get_comm(url):
    comms= []
    header = {
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Accept - encoding": "gzip, deflate, br",
        "Cookie": "uss=WvcTf%2Fm0FVNmFsJTmyzfORO5c5j7e%2ByfWEBy4a%2FlVsc9fGhbZBLCzdGTPg%3D%3D; _m_h5_tk=02350c868a5edde2bc970cac800368c6_1505893868202; _m_h5_tk_enc=33952373d6576df9977c52b9e9bbccb1; cna=6ddIElTq+hQCAXFshQLlWDhg; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; isg=Avj4F8WQ1ZlDFjl5a5uLEG-HyaZKyVVV7xLuCDJq_zOUTYg32nNce8stc3OG; hng=CN%7Czh-CN%7CCNY%7C156; uc1=cookie14=UoTcCfOicyCJkg%3D%3D; uc3=sg2=AVH%2FkEb8%2Bgdy3jLSerMFMambpOr2BLqt5zmUjIVupTs%3D&nk2=AQuN88GK&id2=VAMVeCmJEWbD&vt3=F8dBzWjJcyKPrrWrO5c%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; t=dcf7cbf1344fe32442371f734409967a; tracknick=bonehj; lgc=bonehj; _tb_token_=563ae5137ef55; cookie2=3f19758d9dc2fae097b909005a7262ea"
    }
    req = request.Request(url=url, headers=header)
    response = request.urlopen(req)
    content = response.read().decode('gbk')
    data = str(content)
    data = '{'+data+'}'
    datajson  = simplejson.loads(data)
    rateDatail = datajson["rateDetail"]
    paginator = rateDatail["paginator"]
    lastPage = paginator['lastPage']
    for i in range(0,lastPage):
        time.sleep(5)
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
        for rate in rateList:
            comm ={}
            comm["id"] = rate["id"]
            comm["sku"] = rate["auctionSku"]
            comm["nickname"] = rate["displayUserNick"]
            comm["date"] = rate["rateDate"]
            comm["content"] = rate["rateContent"]
            comm["pics"] = rate["pics"]
            comms.append(comm)
    return comms