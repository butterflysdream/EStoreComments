from django.conf.urls import url
from .views import home,dealComm,buyershow
app_name = 'CommentsSys'
urlpatterns = [
    url(r'^$', home,name='home'),
    url(r'^dealcomm/$',dealComm,name='dealcomm'),
    url(r'^buyershow/$', buyershow, name='buyershow'),
]
