# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class JobsPosts(models.Model):
    jobtitle = models.CharField(max_length = 200)
    jobdescription = models.TextField(null=True)
    requiredexperience = models.TextField(null=True)
    salary = models.TextField(null=True)
    companyname = models.CharField(max_length = 200,null=True)
    companydescription = models.TextField(null=True)
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    logo = models.ImageField(blank=True,null=True, upload_to="blogposts/")
    location = models.CharField(max_length = 200,null=True)
    applylink = models.CharField(max_length = 200,null=True)
    companywebsite = models.TextField(null=True)

    def __str__(self):
        return self.jobtitle
    class Meta:
        verbose_name_plural = "JobsPosts"
