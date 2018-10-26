from django.shortcuts import render

def home(request):
	if request.method == 'GET':
		return render(request, 'blog/home.html')

def home2(request):
	return render(request, 'blog/home2.html')