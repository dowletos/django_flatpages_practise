from django.shortcuts import render,redirect


def mainpage(request):


    return render(request, 'flatpages/main.html', { 'title': 'Добро пожаловать'})