from django.views.generic import TemplateView
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


class HomeView(TemplateView):
    template_name = "index.html"