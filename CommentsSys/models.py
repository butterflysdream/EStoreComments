from django.db import models

# Create your models here.
class ProductInfo(models.Model):
    p_name = models.CharField(max_length=300,verbose_name='产品名称')
    p_brand = models.CharField(max_length=300,validators='品牌')
    p_price = models.FloatField(max_length=6,verbose_name='价格')
    p_image = models.URLField(verbose_name='图片地址')
    p_url = models.URLField(verbose_name='商品地址')
    p_id = models.IntegerField(verbose_name='商品ID')
    p_platform = models.CharField(max_length=20,verbose_name='电商平台',default='淘宝')


class ProductComment(models.Model):
    p_id = models.ManyToOneRel()
