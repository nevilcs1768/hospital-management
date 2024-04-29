from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    
    path('',views.home,name='index'),
    path('news-details/',views.news1,name='detail'),
    path('read-stories/',views.stories1,name='stories'),
    path('appointment',views.appoint1,name='appointments'),
]
