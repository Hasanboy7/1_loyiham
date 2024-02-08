from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="index"),
    path('home/',home,name="home"),
    path('our_work/',our,name="our"),
    path('what_we_do/',what,name="what"),
    path('about_us/',about,name="about"),
    path('get_in_touch/',get,name="get"),
]
