from django.urls import path,include
from . import views

app_name='RailYatra'
urlpatterns = [
    path('index/',views.IndexView.as_view(),name='index'),
    path('signup/',views.signup,name='signup'),
    path('', include('django.contrib.auth.urls'),name='login'),
    
    
]