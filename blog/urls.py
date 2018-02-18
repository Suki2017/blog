from django.conf.urls import url
from . import views


app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tech/$', views.posts, name='posts'),
    url(r'^tech/post/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^tech/category/(?P<category_id>[0-9]+)/$', views.category, name='category-post'),

    url(r'^post/(?P<post_id>[0-9]+)/thank/$', views.add_thank, name='add-thank'),
    url(r'^post/edit/$', views.edit_post, name='edit-post'),

    url(r'^notes/$', views.notes, name='notes'),
    url(r'^thinks/$', views.thinks, name='thinks'),
    url(r'^message/$', views.message, name='message'),
    url(r'^about/$', views.about, name='about'),

]



