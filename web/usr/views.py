from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'usr/dashboard.html')

def decks(request):
	return render(request, 'usr/decks.html')