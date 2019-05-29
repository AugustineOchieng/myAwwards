# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-26 09:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('creation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='sample_img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='landing_page/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(upload_to='profiel_pic/'),
        ),
    ]
