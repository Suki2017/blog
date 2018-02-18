from django.conf.urls import url
from . import views


app_name = 'user_auth'
urlpatterns = [
    url(r'^quick-register/$', views.quick_register, name='quick_register'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user-login/$', views.user_login, name='user_login')
]



