from django.shortcuts import render

# Create your views here.

from django.views.generic import View,ListView
from app.models import *


class HomeView(View):
    def get(self,request):
        return render(request,'app/home.html')


class School_ListView(ListView):
    model=School
    context_object_name='schools'
    ordering=['-name']
    #queryset=School.objects.filter(id=2)
    #template_name='app/school_list.html'



'''
    listView----->  appname/modelname_list.html
    DetailView------->appname/modelname_detail.html

    CreateView----->app/modelname_form.html----------->UpdateView
    DeleteView------->app/modelname_confirm_delete.html
'''