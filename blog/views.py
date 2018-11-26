# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import BlogPosts

# Create your views here.\

def blog(request):

    Posts = BlogPosts.objects.order_by('-created_at')
    context = {
        'Posts': Posts
    }

    return render(request, 'blog/blog.html', context)

# def postDetail(request, pk):
#     BlogPosts.objects.get(pk=pk)

def postDetail(request, pk):
    Posts = BlogPosts.objects.get(pk=pk)
    context = {
        'Posts': Posts
    }
    return render(request, 'blog/postDetail.html', context)