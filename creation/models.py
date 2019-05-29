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

  @classmethod
  def search_by_title(cls,search_term):
      sample_img = cls.objects.filter(title__icontains=search_term)
      return sample_img

  @classmethod
  def search_by_title(cls,search_term):
      sample_img = cls.objects.filter(category__icontains = search_term)
      return sample_img


  def __str__(self):
        return self.title

class Profile(models.Model):
  profile_picture = models.ImageField(upload_to='profiel_pic/')
  bio = models.CharField(max_length=100)
  project = models.ForeignKey(Project)
  contact = models.CharField(max_length=30)
  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

class Comment(models.Model):
  project_id = models.IntegerField(default=0) 
  # reply = models.ForeignKey('self', null=True, related_name='replies')
  content = HTMLField()
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