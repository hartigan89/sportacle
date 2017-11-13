from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^$', views.RegistrationFormView.as_view(), name='landing'),
    url(r'^login/$', login, {'template_name' : 'application/login.html'}, name='login'),
    url(r'^logout/$', logout, {'next_page' : 'landing'}, name='logout'),
    url(r'^faq/$', views.faq,  name='faq'),
    ]