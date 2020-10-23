from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.db.models import Avg, Max, FloatField, Count, Q

from .forms import SquirrelRequestForm,LatiForm
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

def update_lati(request, squirrel_id):
    if request.method == 'POST':
        sighting = get_object_or_404(SquirrelDetails, pk=squirrel_id)
        form = LatiForm(request.POST or None,
                        request.FILES or None, instance=sighting)
        if form.is_valid():
            form.Latitude = form.cleaned_data['Latitude']
            form.Longitude = form.cleaned_data['Longitude']
            form.Shift = form.cleaned_data['Shift']
            form.Date = form.cleaned_data['Date']
            form.Age = form.cleaned_data['Age']
            form.save()
            context = {'form': form}
        next = request.POST.get('next', '/')
        return HttpResponseRedirect(next) 
    else:
        return JsonResponse({'errors': form.errors}, status=400)
    
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
    am_counts = SquirrelDetails.objects.filter(Shift__exact='AM').count()
    pm_counts = SquirrelDetails.objects.filter(Shift__exact='PM').count()
    adult_counts = SquirrelDetails.objects.filter(Age__exact='Adult').count()
    juvenile_counts = SquirrelDetails.objects.filter(Age__exact='Juvenile').count()
    gray_counts = SquirrelDetails.objects.filter(Primary_Fur_Color__exact='Gray').count()
    cinnamon_counts = SquirrelDetails.objects.filter(Primary_Fur_Color__exact='Cinnamon').count()
    running_counts = SquirrelDetails.objects.filter(Running__exact='True').count()
    
    context={
        'counts':counts,
        'am_counts':am_counts,
        'pm_counts':pm_counts,
        'adult_counts':adult_counts,
        'juvenile_counts':juvenile_counts,
        'gray_counts':gray_counts,
        'cinnamon_counts':cinnamon_counts,
        'running_counts':running_counts,
    }
    return render(request,'squirrelapp/sightingsstats.html',context)

