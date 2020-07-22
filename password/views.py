from django.shortcuts import render


def home(request):
    return render(request, 'password/homepage.html')


def password(request):
    return render(request, 'password/password.html')
