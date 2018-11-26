# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import JobsPosts

# Create your views here.\

def jobs(request):

    JPosts = JobsPosts.objects.order_by('-created_at')
    context = {
        'JPosts': JPosts
    }

    return render(request, 'jobs/jobs.html', context)

# def postDetail(request, pk):
#     BlogPosts.objects.get(pk=pk)

def jobsDetail(request, pk):
    JPosts = JobsPosts.objects.get(pk=pk)
    context = {
        'JPosts': JPosts
    }
    return render(request, 'jobs/jobsDetail.html', context)