from django.contrib import admin
from django.urls import path,include
from.import views
#from django.conf.urls import url
from new_pjt_app.views import index2


urlpatterns = [
    
    path('',index2.as_view(),name='index2'),
   
]