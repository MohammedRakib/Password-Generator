from django.shortcuts import render
import random

def home(request):
    return render(request, 'password/homepage.html')


def password(request):

    character = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        character.extend(list('1234567890'))
    if request.GET.get('special'):
        character.extend(list('!@#$%^&*()'))
    length = int(request.GET.get('length', 8))
    pass_generated = ''
    for i in range(length):
        pass_generated += random.choice(character)

    return render(request, 'password/password.html', {'password': pass_generated})

def about(request):
    return render(request,'password/about.html')
