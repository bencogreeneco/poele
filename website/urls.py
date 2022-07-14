from django.urls import path
from website import views
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
]