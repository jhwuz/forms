from django.shortcuts import render, redirect
from .models import Post
from .forms import NameForm, PostForm, ContactForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# simple form
def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'form/render-name.html', {'data': form.cleaned_data})
    else:
        form = NameForm()
    return render(request, 'form/name.html', {
        'form': form,
        'title': 'Simple Form',
    })


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             f'Your account has been created, {form.cleaned_data.get("username")}. You may now login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'form/register.html', {
        'form': form,
        'title': 'Register',
    })


def home(request):
    context = {
        'data': request.POST,
        'title': 'Home',
        'posts': Post.objects.all()
    }
    return render(request, 'form/home.html', context)


@login_required
def make_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'form/post.html', {
        'form': form,
        'title': 'Make Post',
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form/render-contact.html', {'data': form.cleaned_data})

    else:
        form = ContactForm()
    return render(request, 'form/post.html', {
        'form': form,
        'title': 'Make Post',
    })
