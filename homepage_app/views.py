from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.

def index(request):
	datas = Data.objects.all()
	content = {'datas': datas}
	return render(request, 'homepage_app/index.html', content)
	# return HttpResponse("hi")

def saveData(request):
	sex = ['Male', 'Female']
	data = Data()
	data.name = request.POST['name']
	data.sex = request.POST['sex']
	data.ages = request.POST['ages']
	data.save()
	return HttpResponseRedirect(reverse('index1'))

def sendData(request):
	datas = Data.objects.all()
	content = {'datas': datas}
	return render(request, 'homepage_app/index.html', content)





























