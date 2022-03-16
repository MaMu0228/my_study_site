from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'homepage_app/index.html')
	# return HttpResponse("hi")





















