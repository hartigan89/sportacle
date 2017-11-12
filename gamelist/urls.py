from django.conf.urls import url
from gamelist import views

urlpatterns = [
url(r'^(?P<sport_slug>[-\w.]+)/$', views.GameList, name='game_list_by_sport'),
url(r'', views.GameList, name='gamelist'),
]