from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^account/', include('user_auth.urls')),
    url(r'^account/', include('django.contrib.auth.urls')),
    url(r'^common/', include('common.urls')),

]
