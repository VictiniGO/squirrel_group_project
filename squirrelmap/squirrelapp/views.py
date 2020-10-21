from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import SquirrelDetails


def map(request):
    sightings = SquirrelDetails.objects.all()[:100]
    context = {
            'sightings': sightings,
    }
    return render(request,'squirrelapp/map.html',context)

def index(request):
    sightings = SquirrelDetails.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request,'squirrelapp/index.html',context)

def update(request, squirrel_id):
    sighting = get_object_or_404(SquirrelDetails, pk=squirrel_id)
    context = {
            'sighting': sighting,
    }
    return render(request,'squirrelapp/update.html',context)

def sightingsadd(request):
    return render(request,'squirrelapp/sightingsadd.html',{})

def sightingsstats(request):
    return render(request,'squirrelapp/sightingsstats.html',{})
   
