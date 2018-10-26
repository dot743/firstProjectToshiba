from django.urls import path
from .views import *

urlpatterns = [
    path('tan', home),
    path('2', home2),

]
