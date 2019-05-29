  
from django import forms
from .models import  Project, Profile, Comment, Vote



   
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['user']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'project', 'date_posted', 'reply']
        
class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        exclude=['user','project']
