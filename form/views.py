from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import NameForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


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


# model form
def get_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'form/render-user.html', {'data': form.cleaned_data})
    else:
        form = UserForm()
    return render(request, 'form/user.html', {
        'form': form,
        'title': 'Model User',
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
    }
    return render(request, 'form/home.html', context)
