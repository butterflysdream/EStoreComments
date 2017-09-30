from django.conf.urls import url
from .views import home,dealComm

urlpatterns = [
    url(r'^$', home,name='home'),
    url(r'^dealcomm/$',dealComm,name='dealcomm'),
]
