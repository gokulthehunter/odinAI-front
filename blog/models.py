# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class BlogPosts(models.Model):
    posttitle = models.CharField(max_length = 200)
    postsummary = models.TextField(null=True)
    postcontent = models.TextField(null=True)
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    image = models.ImageField(blank=True,null=True, upload_to="blogposts/")
    authorfirstname = models.CharField(max_length = 200,null=True)
    authorlastname = models.CharField(max_length = 200,null=True)
    authorbg = models.TextField(null=True)
    authordesignation = models.TextField(null=True)
    authorcontact = models.TextField(null=True)

    def __str__(self):
        return self.posttitle
    class Meta:
        verbose_name_plural = "BlogPosts"
