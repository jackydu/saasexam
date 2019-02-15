# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

# Create your models here.


class SaasExamJacky(models.Model):
    name = models.CharField(max_length=128)
    mobile = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
