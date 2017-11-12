from django.conf.urls import url
from mysportacle import views

urlpatterns = [
    url(r'^(?P<username>[-\w.]+)/$', views.profile_page, name='profile'),
    url(r'^(?P<username>[-\w.]+)/followers/$', views.list_followers, name='list_followers'),
    url(r'^(?P<username>[-\w.]+)/following/$', views.list_following, name='list_following'),
    url(r'^add/(?P<user_id>\d+)/$', views.follow, name='profile_follow'),
    url(r'^remove/(?P<user_id>\d+)/$', views.unfollow, name='profile_unfollow'),
]