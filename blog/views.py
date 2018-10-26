from django.shortcuts import render
from .models import *

def home(request, flipper):
	if request.method == 'GET':
		post = Post.objects.get(id=flipper)
		return render(request, 'blog/home.html', {'post':post})

def home2(request):
	return render(request, 'blog/home2.html')