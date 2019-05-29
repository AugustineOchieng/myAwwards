# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Project, Profile, Comment, Vote

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Vote)
