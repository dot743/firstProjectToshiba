from django.urls import path
from .views import *

urlpatterns = [
    path('tan/<int:flipper>', home),
    path('2', home2),
]
