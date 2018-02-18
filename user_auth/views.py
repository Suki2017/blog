from uuid import uuid4

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import make_password
from django.utils import timezone

from .utils import user_auth
from .models import Info
from .forms import RegisterForm


def quick_register(request):
    email = request.POST.get('user')
    pwd = request.POST.get('pwd')
    User.objects.create(
        username=uuid4().hex[:8],
        email=email,
        password=make_password(pwd),
        is_superuser=False,
        last_login=timezone.now()
    )
    return JsonResponse({'OK': 'success'}, status=201)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'user_auth/register.html', context={'form': form})


def user_login(request):
    act = request.POST.get('user')
    pwd = request.POST.get('pwd')
    user = user_auth(act, pwd)
    if user is None:
        return JsonResponse({'LoginFailed': 'invalid data for login'}, status=400)
    login(request, user)
    return JsonResponse({'Success': 'OK'}, status=200)


def user_logout(request):
    logout(request)
    return redirect(request.GET.get('next'))


def index(request):
    return render(request, 'index.html')

