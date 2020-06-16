# from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from user.views import login, register, revise, forget, index, upload

urlpatterns = [
    path('login/', login),
    path('register/',register),
    path('revise/',revise),
    path('forget/',forget),
    path('index/',index),
    path('upload/',upload)

]