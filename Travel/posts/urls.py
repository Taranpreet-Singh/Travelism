from django.conf.urls import url
from . import views

app_name= 'posts'

urlpatterns = [
    url(r'^new/$', views.CreatePost.as_view(), name='create'),
    url(r'^$', views.PostList.as_view(), name='post_list'),
]
