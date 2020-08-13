from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class FirstView(View):
    def get(self, request):
        text = 'All ok'
        return render(request, 'main_page.html', locals())


class NewTechnology(View):
    def get(self, request):
        return render(request, 'new_technology.html', locals())


class NewCureTechnology(View):
    def get(self, request):
        return render(request, 'new_cure_technology.html')
