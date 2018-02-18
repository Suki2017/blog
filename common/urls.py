from django.conf.urls import url
from common import views


app_name = 'common'
urlpatterns = [
    url(r'^upload-image/$', views.upload_image, name='upload_image'),

]
