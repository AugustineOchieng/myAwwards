# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Profile, Comment
from .forms import NewProfileForm, NewProjectForm, CommentForm, VoteForm
from django.core.exceptions import ObjectDoesNotExist
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
  return render(request, 'single_project.html', contextual)
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
        user = Profile.objects.get(user=request.user)
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
        profiles = Profile.objects.get(user=current_user)
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
        return redirect('NewProfile')

    else:
        form = NewProfileForm()
        return render(request, 'new_profile.html', {"form": form})
     
@login_required(login_url='/accounts/login/')  
def new_comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            # project.poster_id = current_user.id
            comment.save()
        return redirect('single_p')

    else:
        form = CommentForm()
    return render(request, 'new_comment.html', {"form": form})

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
        index_path = Project.objects.filter(id = single_id)
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
@login_required(login_url='/accounts/login/')
def add_review(request,pk):
   project = get_object_or_404(Project, pk=pk)
   current_user = request.user
   if request.method == 'POST':
       form = ReviewForm(request.POST)
       if form.is_valid():
           design = form.cleaned_data['design']
           usability = form.cleaned_data['usability']
           content = form.cleaned_data['content']
           review = form.save(commit=False)
           review.project = project
           review.juror = current_user
           review.design = design
           review.usability = usability
           review.content = content
           review.save()
           return redirect('one_page')
   else:
       form = ReviewForm()
       return render(request,'review.html',{"user":current_user,"form":form})