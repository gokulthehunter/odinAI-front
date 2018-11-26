# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class CollegePosts(models.Model):
    cposttitle = models.CharField(max_length = 200)
    cpostsummary = models.TextField(null=True)
    cpostcontent = models.TextField(null=True)
    ccreated_at = models.DateTimeField(default = datetime.now, blank = True)
    cimage = models.ImageField(blank=True,null=True, upload_to="collegeposts/")
    cauthorfirstname = models.CharField(max_length = 200,null=True)
    cauthorlastname = models.CharField(max_length = 200,null=True)
    cauthorbg = models.TextField(null=True)
    cauthordesignation = models.TextField(null=True)
    cauthorcontact = models.TextField(null=True)

    def __str__(self):
        return self.cposttitle
    class Meta:
        verbose_name_plural = "CollegePosts"
