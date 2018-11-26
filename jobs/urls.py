from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.jobs,name = "job"),
    url(r'^(?P<pk>\d+)$', views.jobsDetail, name="jobsDetail")
]
