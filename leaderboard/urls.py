from django.conf.urls import url
from leaderboard import views

urlpatterns = [
url(r'', views.leaderboard_page, name='leaderboard'),
]