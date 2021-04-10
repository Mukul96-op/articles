from django.shortcuts import render , redirect , get_object_or_404

from authy.forms import SignUpForm ,EditProfileForm , ChangePasswordForm
from django.contrib import messages

from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.core.paginator import Paginator

from authy.models import Profile

# Create your views here.
def UserProfile(request,username):
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user = user)
    articles = profile.favorites.all()

    #Pagination
    paginator = Paginator(articles,6)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)


    context= {
        'articles':articles_paginator,
        'profile':profile,
    }

    return render(request , 'profile.html',context)

def Signup(request):
    pyt
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            confirm_password = form.cleaned_data.get('confirm_password')

            User.objects.create_user(username= username, email=email, password=password, first_name=first_name, last_name=last_name)
            return redirect('home')

    else:
        form = SignUpForm()
    context = {
        'form': form,
    }

    return render(request, 'signup.html', context)    

@login_required
def PasswordChange(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request ,user)
            return redirect('change_password_done')
    else:
        form = ChangePasswordForm(instance =user)
   
    context={
        'form':form,
    }
    return render(request, 'change_password.html' , context)

def ChangePasswordDone(request):
    return render(request,'change_password_done.html')

@login_required
def EditProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user__id = user)
    categories = Category.objects.all()

    if request.method =="POST":
        form = EditProfileForm(request.POST , request.FILES)
        if form.is_valid():
            profile.picture = form.cleaned_data.get('picture')
            profile.first_name = form.cleaned_data.get('first_name')
            profile.last_name = form.cleaned_data.get('last_name')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.profile_info = form.cleaned_data.get('profile_info')
            profile.save()

            return redirect('home')
    else:
        form = EditProfileForm()
    
    context = {
        'form':form,
    }

    return render(request,'edit_profile.html',context)

