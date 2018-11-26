from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.blog,name = "blog"),
    url(r'^(?P<pk>\d+)$', views.postDetail, name="postDetail")
]
