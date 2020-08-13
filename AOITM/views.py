from django.shortcuts import render
from django.views import View


class LandingPage(View):

    def get(self, request):
        foundations = []
        organizations = []
        local_collections = []
        return render(request, 'index.html', locals())
