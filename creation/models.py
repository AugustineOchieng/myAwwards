# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Project(models.Model):
  title=models.CharField(max_length =30)
  link = models.CharField(max_length=100)
  description = models.CharField(max_length=100)
  sample_img = models.ImageField(upload_to='landing_page/')

 

  def __str__(self):
        return self.title

class Profile(models.Model):
  profile_picture = models.ImageField(upload_to='profiel_pic/')
  bio = models.CharField(max_length=100)
  project = models.ForeignKey(Project)
  contact = models.CharField(max_length=30)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
  project = models.ForeignKey(Project)
  # reply = models.ForeignKey('self', null=True, related_name='replies')
  content = models.TextField(max_length=100)
  date_posted = models.DateTimeField(default=timezone.now)
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='replicate')
  def __str__(self):
        return self.content

class Vote(models.Model):
  design=models.IntegerField(default=0,validators=[MaxValueValidator(20)])
  usability=models.IntegerField(default=0,validators=[MaxValueValidator(20)])
  content=models.IntegerField(default=0,validators=[MaxValueValidator(20)])
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  project=models.IntegerField(default=0)