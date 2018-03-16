"""mysite URL Configuration
"""

from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('blog.urls')),
    url(r'^dimsm.pythonanywhere.com1/', include('blog.urls')),
]
