"""laramieduncan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from website import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^about', views.about),
    url(r'^services', views.services),
    url(r'^404', views.four_o_four),
    url(r'^faq', views.faq),
    url(r'^pricing', views.pricing),
    url(r'^portfolio-1-col', views.portfolio_1_col),
    url(r'^portfolio-2-col', views.portfolio_2_col),
    url(r'^portfolio-3-col', views.portfolio_3_col),
    url(r'^portfolio-4-col', views.portfolio_4_col),
    url(r'^portfolio-item', views.portfolio_item),
    url(r'^full-width', views.full_width),
    url(r'^contact', views.contact),
    url(r'^blog-home-1', views.blog_home_1),
    url(r'^blog-home-2', views.blog_home_2),
    url(r'^blog-post', views.blog_post),
    url(r'^sidebar', views.sidebar),
]
