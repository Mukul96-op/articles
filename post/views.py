from django.shortcuts import render, get_object_or_404 , redirect
from post.models import Post, Category, Tag ,Contact
from post.forms import ContactForm
from django.utils import timezone
from django.core.paginator import Paginator

from django.db.models import Q
from authy.models import Profile


# Create your views here.


def home(request):
    articles = Post.objects.filter(
        status='published').order_by('-publication_date')
    categories = Category.objects.all()
    
    #SEARCH
    query = request.GET.get("q")
    if query:
        articles = articles.filter(Q(title__icontains=query)| Q(content__icontains= query)).distinct()
    
    #Pagination
    paginator = Paginator(articles,6)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)

    context = {
        'articles': articles_paginator,
        'categories': categories,
    }
    
    return render(request, 'home.html', context)


def category(request, category_slug):
    articles = Post.objects.filter(
        status='published').order_by('-publication_date')
    categories = Category.objects.all()

    if category_slug:
        category = get_object_or_404(Category,  slug=category_slug)
        articles = articles.filter(category=category)
    
     #SEARCH
    query = request.GET.get("q")
    if query:
        articles = articles.filter(Q(title__icontains=query)| Q(content__icontains= query)).distinct()

    #Pagination
    paginator = Paginator(articles,6)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)

    context = {
        'articles': articles_paginator,
        'categories': categories,
    }

    return render(request, 'category.html', context)


def tags(request, tag_slug):
    tags = Tag.objects.all()
    articles = Post.objects.filter(
        status='published').order_by('-publication_date')
    categories = Category.objects.all()

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        articles = articles.filter(tags=tag)
    
     #SEARCH
    query = request.GET.get("q")
    if query:
        articles = articles.filter(Q(title__icontains=query)| Q(content__icontains= query)).distinct()

    #Pagination
    paginator = Paginator(articles,6)
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)

    context={
        'articles': articles_paginator,
        'categories':categories,
    }

    return render(request,'tag.html',context)

def postDetail(request,post_slug):
    article = get_object_or_404(Post , slug = post_slug)
    user    = request.user.id
    profile = Profile.objects.get(user_id = user)

    if profile.favorites.filter(slug = post_slug).exists():
        fav = True
    else:
        fav = False

    if request.method =="POST":
        if profile.favorites.filter(slug = post_slug).exists():
            profile.favorites.remove(article)
        else:
            profile.favorites.add(article)
            

    categories = Category.objects.all()
    context={
        'article': article,
        'categories':categories,
        'fav':fav,
    }

    return render(request,'post_detail.html',context)

def Contact(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save(commit =False)
            message.message_date = timezone.now()
            form.save()
            return redirect('contactsuccess')
    else:
        form = ContactForm()

    context={
        'form':form,
        'categories':categories,
    }

    return render(request , 'contact.html',context)

#static website for the form contact

def ContactSuccess(request):
    return render(request,'contactsuccess.html')