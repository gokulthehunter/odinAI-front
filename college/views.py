# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import CollegePosts

# Create your views here.\

def collegeblog(request):

    CPosts = CollegePosts.objects.order_by('-ccreated_at')
    context = {
        'CPosts': CPosts
    }

    return render(request, 'college/college.html', context)

# def postDetail(request, pk):
#     BlogPosts.objects.get(pk=pk)

def cpostDetail(request, pk):
    CPosts = CollegePosts.objects.get(pk=pk)
    context = {
        'CPosts': CPosts
    }
    return render(request, 'college/collegeDetail.html', context)