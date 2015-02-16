# coding=utf-8

#from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from reblog.settings import redis_con


class HomeView(TemplateView):
    template_name = 'main/home.html'
