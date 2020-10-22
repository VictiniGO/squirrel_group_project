from django.urls import reverse
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import SquirrelRequestForm
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
    if request.method == 'POST':
        form = SquirrelRequestForm(request.POST)

        if form.is_valid():
            form.Latitude = form.cleaned_data['Latitude']
            form.Longitude = form.cleaned_data['Longitude']
            form.Unique_Squirrel_ID = form.cleaned_data['Unique_Squirrel_ID']
            form.Shift = form.cleaned_data['Shift']
            form.Age = form.cleaned_data['Age']

            form.save()
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = SquirrelRequestForm()
    return render(request,'squirrelapp/sightingsadd.html',{'form':form})

def sightingsstats(request):
    counts = SquirrelDetails.objects.count()
    return render(request,'squirrelapp/sightingsstats.html',{})
   
