from django.urls import path
#from . import views 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    #path('index/', views.index, name='index')
]

