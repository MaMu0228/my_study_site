from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index1"),
	path('save', views.saveData, name="save"),
	path('getData', views.sendData, name="sendData")

]
