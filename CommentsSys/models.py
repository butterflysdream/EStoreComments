from django.db import models

# Create your models here.
class ProductInfo(models.Model):
    p_name = models.CharField(max_length=300,verbose_name='产品名称')
    p_brand = models.CharField(max_length=300,verbose_name='品牌')
    # p_price = models.FloatField(max_length=6,verbose_name='价格')
    p_info = models.TextField(verbose_name='商品信息',blank=True,null=True)
    p_image = models.URLField(verbose_name='图片地址')
    p_url = models.URLField(verbose_name='商品地址')
    p_id = models.IntegerField(verbose_name='商品ID')
    p_platform = models.CharField(max_length=20,verbose_name='电商平台',default='淘宝')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = "商品"

class ProductComm(models.Model):
    product = models.ForeignKey(ProductInfo)
    comm_sku = models.CharField(max_length=300,verbose_name="SKU",blank=True,null=True)
    comm_id = models.BigIntegerField(verbose_name='评论ID',blank=True,null=True)
    comm_nickname = models.CharField(max_length=100,verbose_name='用户昵称',blank=True,null=True)
    comm_date = models.DateTimeField(verbose_name='评论时间',blank=True,null=True)
    comm_content = models.TextField(max_length=2000,null=True,blank=True,verbose_name='评论');

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = "评论"

class ProductCommImage(models.Model):
    product_comm = models.ForeignKey(ProductComm)
    imageUrl = models.URLField(verbose_name='买家秀地图片')
