from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.collegeblog,name = "collegeblog"),
    url(r'^(?P<pk>\d+)$', views.cpostDetail, name="cpostDetail")
]
