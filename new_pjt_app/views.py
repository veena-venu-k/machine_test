from multiprocessing import context
from sunau import Au_read
from termios import N_MOUSE
from django.shortcuts import render, redirect
from .forms import User_Form
from django.http import HttpResponse
from.models import first_model
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from new_pjt_app.models import first_model
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView, DeleteView, UpdateView, RedirectView
from django.http import request
from django.views import View
import json
from django.http import JsonResponse





class index2(TemplateView):
    template_name = "second_pg.html"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = User_Form()
        au = first_model.objects.all()
        context = {'show':au, 'form':fm}
        return context
    
    form_class = User_Form
    def post(self, *args, **kwargs):
        if self.request.is_ajax and self.request.method == "POST" :
            fm = self.form_class(self.request.POST)
            
            if fm.is_valid():
                fm.save()
                return JsonResponse({"Sucess": True}, status=200)
            else:
                return JsonResponse({"error": fm.errors}, status=400)

        return JsonResponse({"error": ""}, status=400) 



               
                

