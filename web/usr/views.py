from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def home(request):
	lastset = Sets.objects.raw("select name,code,date from mtg_schema.sets order by substring(date,4,4) desc,substring(date,1,2) desc")[0]
	totalcards = Cards.objects.count()

	return render(request, 'usr/dashboard.html', {'lastset':lastset, 'totalcards':totalcards})

def decks(request):
	decks = Decks.objects.raw("select id,name,format from mtg_schema.decks")

	return render(request, 'usr/decks.html', {'decks': decks})