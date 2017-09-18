import json
from urllib import request

import simplejson


def spider():
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=545655851754&spuId=723713456&sellerId=2129855716';
    response = request.urlopen(url)
    content = response.read()
    print(content)
    data = str(content.decode('raw_unicode_escape'))

    # data.replace("\\r\\n\\r\\n",'',0)
    # print(data[10:])
    data = '{'+data+'}'
    print(data)
    datajson  = simplejson.loads(data)
    rateDatail = datajson["rateDetail"]
    paginator = rateDatail["paginator"]
    page = paginator['page']
    print(page)

if __name__ == "__main__":
    spider();
    