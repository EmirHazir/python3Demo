from django.conf.urls import url
from .views import post_create,post_delete,post_detail,post_index,post_update

urlpatterns = [
    url(r'^index/$', post_index),
    url(r'^(?P<id>\d+)/$', post_detail),
    url(r'^create/$' ,post_create),
    url(r'^update/$', post_update),
    url(r'^delete/$', post_delete),
]