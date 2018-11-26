# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPosts
from college.models import CollegePosts
# Create your views here.\

def index(request):

    Posts = BlogPosts.objects.order_by('-created_at')[0:2]
    CPosts = CollegePosts.objects.order_by('-ccreated_at')[0:2]
    context = {
        'Posts': Posts,
        'CPosts': CPosts
    }

    return render(request, 'home/index.html', context)
