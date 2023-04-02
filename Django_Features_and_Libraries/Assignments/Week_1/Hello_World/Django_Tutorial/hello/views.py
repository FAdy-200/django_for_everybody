from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.
class IndexView(View):
    def get(self,request):
        num_visits = request.session.get('num_visits', 0) + 1
        request.session['num_visits'] = num_visits 
        if num_visits > 4 : request.session.pop('num_visits')
        resp = HttpResponse('view count='+str(num_visits))
        resp.set_cookie('dj4e_cookie', '4e8c6d5e', max_age=1000)
        return resp