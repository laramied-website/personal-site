# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def four_o_four(request):
    return render (request, '404.html')

def about(request):
    return render (request, 'about.html')

def blog_home_1(request):
    return render (request, 'blog-home-1.html')

def blog_home_2(request):
    return render (request, 'blog-home-2.html')

def blog_post(request):
    return render (request, 'blog-post.html')

def contact(request):
    return render (request, 'contact.html')

def faq(request):
    return render (request, 'faq.html')

def full_width(request):
    return render (request, 'full-width.html')

def index(request):
    return render (request, 'index.html')

def portfolio_1_col(request):
    return render (request, 'portfolio-1-col.html')

def portfolio_2_col(request):
    return render (request, 'portfolio-2-col.html')

def portfolio_3_col(request):
    return render (request, 'portfolio-3-col.html')

def portfolio_4_col(request):
    return render (request, 'portfolio-4-col.html')

def portfolio_item(request):
    return render (request, 'portfolio-item.html')

def pricing(request):
    return render (request, 'pricing.html')

def services(request):
    return render (request, 'services.html')

def sidebar(request):
    return render (request, 'sidebar.html')