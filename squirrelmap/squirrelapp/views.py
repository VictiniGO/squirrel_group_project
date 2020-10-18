from django.shortcuts import render
from django.http import HttpResponse

def map(request):
    return render(request,'squirrelapp/map.html',{})

def sightingslist(request):
    return render(request,'squirrelapp/sightings.html',{})

def sightingsadd(request):
    return render(request,'squirrelapp/sightingsadd.html',{})

def sightingsstats(request):
    return render(request,'squirrelapp/sightingsstats.html',{})
   
