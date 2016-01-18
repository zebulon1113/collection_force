"""ctfeshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from collection import views as collection_view

collection_force_urlpatterns = [ 
    url(r'^wechat/(\w{1,})/', collection_view.wechat_url ),
    url(r'^person/', collection_view.person ),
    url(r'^force/', collection_view.update_force ),
    url(r'^share/', collection_view.reward ),
    url(r'^reward/', collection_view.reward ),
]


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', collection_view.login ),
    url(r'api/', include(collection_force_urlpatterns)),
]
