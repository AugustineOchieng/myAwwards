from rest_framework import serializers
from .models import Project
from .models import Profile
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ['profile_picture','user','project']
       

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ['link','sample_img',]
       
