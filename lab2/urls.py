"""Form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from .views import project, post_new, post_detail, post_search, adddata

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^project/', project),
url(r'^post/', post_detail, name='post_detail'),
    url(r'^news', post_new, name='post_new'),
    url(r'^post_search/', post_search, name = 'post search'),
url(r'^adddata/', adddata, name = 'adddata')
]
