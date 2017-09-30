from django.contrib import admin
from .models import ProductInfo,ProductComm,ProductCommImage
# Register your models here.


class InfoAdmin(admin.ModelAdmin):
    list_display = ('p_name','p_brand','p_price','p_image','p_id',)
    search_fields = ( 'product_name',)

class CommAdmin(admin.ModelAdmin):
    list_display = ('product_name','comm_sku','comm_nickname','comm_date','comm_content',)
    search_fields = ('comm_content',)

    def product_name(self, obj):
        return u'%s' % obj.product.p_name

class ImageAdmin(admin.ModelAdmin):
    list_display = ('imageUrl',)
admin.site.register(ProductInfo,InfoAdmin)
admin.site.register(ProductComm,CommAdmin)
admin.site.register(ProductCommImage,ImageAdmin)