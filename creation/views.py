# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Comment
from .forms import NewProfileForm, NewProjectForm, CommentForm, VoteForm
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer
from .serializer import ProjectSerializer
from rest_framework import status

@login_required(login_url='/accounts/login/')  
def home(request):
  context = {
    'projects': Project.objects.all()
  }
  return render(request, 'index.html', context)

@login_required(login_url='/accounts/login/')  
def comment(request):
    contextual = {
    'comments': Comment.objects.all()
    }
    return render(request, 'comments.html', contextual)
# @login_required(login_url='/accounts/login/')
# def profile(request):
#   context = {
#     'profiles': Profile.objects.all()
#   }  
#   return render(request, 'profile.html', context)
@login_required(login_url='/accounts/login/')  
def new_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.profile = current_user
            # project.poster_id = current_user.id
            project.save()
        return redirect('index')

    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {"form": form})
@login_required(login_url='/accounts/login/')  
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        user = Profile.objects.filter(user=request.user).first()
        form = NewProfileForm(request.POST, request.FILES, instance=user)
        profile = Profile.objects.filter(user_id =current_user.id)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = NewProfileForm()
    return render(request, 'edit_profile.html', {'form': form})
@login_required(login_url='/accounts/login/')  
def profile(request):
    current_user = request.user
    # images = Image.objects.filter(profile = current_user)

    try:
        profiles = Profile.objects.filter(user=current_user)
    except ObjectDoesNotExist:
        return redirect('new_profile')

    return render(request, 'profile.html', {'profiles': profiles, 'current_user': current_user})
@login_required(login_url='/accounts/login/')     
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.userId = request.user.id
            profile.save()
        return redirect('index')

    else:
        form = NewProfileForm()
        return render(request, 'new_profile.html', {"form": form})
     
@login_required(login_url='/accounts/login/')  
def new_comment(request, id):
    project = Project.objects.filter(id=id)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.project_id = id
            form.save()
        return redirect('one_project', id)

    else:
        form = CommentForm()
    try:
        user_comment = Comment.objects.filter(project_id=id)
    except Exception as e:
        raise Http404()
    return render(request, 'new_comment.html', {"project":project, "current_user":current_user, "form": form})

def single_project(request):
    context = {
    'projects': Project.objects.all()
    }
    return render(request, 'single_project.html', context)
def voter(request):
    if request.method == 'POST':
        form = VotingForm(request.POST)
        if form.is_valid():
            chosen_categories_options = form.cleaned_data.get('chosen_categories_options', [])
            Vote.bulk_vote(chosen_categories_options)
        message = 'Thank you for your contribution!'
    elif request.method == 'GET':
        message = ''
    form = VotingForm()
    return render(request, 'vote.html', {'form': form, 'message': message})
def single(request,single_id):
    try:
        single = Project.objects.filter(id = single_id)
    except DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = UploadForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()
            return redirect('single')
    else:
        form =  VoteForm()

    return render(request, "single_project.html", locals())
def search_results(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_single = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"single": searched_single})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
class Projecter(APIView):
    def get(self, request, format=None):
        project = Project.objects.all()
        serializers = ProjectSerializer(project, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class Profilel(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializers = ProfileSerializer(profile, many=True)
        return Response(serializers.data)
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
