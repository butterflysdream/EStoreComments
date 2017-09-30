import re
from django.shortcuts import render
from . import taobaoSpider
from .models import ProductComm,ProductInfo,ProductCommImage
# Create your views here.

def home(request):
    return  render(request,'home.html')

def dealComm(request):
    if request.POST:
        url = request.POST['urltext']
        if url =="":
            msg="请输入商品地址！！"
            return render(request, 'home.html', {'msg': msg})
        if "ti" in request.POST.get('submit'):
            result =taobaoSpider.spider(url =url)
            product_r = result["product"]
            comms = result["comms"]
            if not ProductInfo.objects.filter(p_name= product_r["p_name"]).exists():
                product = ProductInfo()
                product.p_id = product_r["itemid"]
                product.p_name = product_r["p_name"]
                product.p_brand = product_r["brand"]
                product.p_image = product_r["imgurl"]
                product.p_url = product_r["url"]
                product.p_price = product_r["price"]
                product.save()
                for comm in comms:
                    pro_comm = ProductComm()
                    pro_comm.product = product
                    pro_comm.comm_content = comm["content"]
                    pro_comm.comm_date = comm["date"]
                    pro_comm.comm_id = comm["id"]
                    pro_comm.comm_nickname = comm["nickname"]
                    pro_comm.comm_sku = comm["sku"]
                    pro_comm.save()
                    for pic in comm["pics"]:
                        comm_pic = ProductCommImage()
                        comm_pic.product_comm = pro_comm
                        comm_pic.imageUrl = pic
                        comm_pic.save()
                return render(request, 'home.html', {'product': product})
            else:
                product = ProductInfo.objects.get(p_id=product_r["itemid"])
                for comm in comms:
                    if not ProductComm.objects.filter(product=product, comm_id = comm["id"]).exists():
                        pro_comm = ProductComm()
                        pro_comm.product = product
                        pro_comm.comm_content = comm["content"]
                        pro_comm.comm_date = comm["date"]
                        pro_comm.comm_id = comm["id"]
                        pro_comm.comm_nickname = comm["nickname"]
                        pro_comm.comm_sku = comm["sku"]
                        pro_comm.save()
                        for pic in comm["pics"]:
                            comm_pic = ProductCommImage()
                            comm_pic.product_comm = pro_comm
                            comm_pic.imageUrl = pic
                            comm_pic.save()
                return render(request, 'home.html',{'product': product})
        if "view" in request.POST.get("submit"):
            itemid = re.findall(re.compile('[0-9]+'), url)[0]
            product = ProductInfo.objects.get(p_id=itemid)
            return render(request, 'home.html', {'product': product})

def buyershow(request):
    images = ProductCommImage.objects.all()
    return render(request, 'buyershow.html',{'images':images})


