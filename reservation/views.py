from django.http import QueryDict
from django.shortcuts import render
from .models import Doc_time, Doctors_profile
from .filters import DoctorsFilter




def search(request):
    docs = Doctors_profile.objects.all()
    Dtimes = Doc_time.objects.all()
    myfilters = DoctorsFilter(request.GET,queryset=docs)
    docs = myfilters.qs
    context = {
        "myfilters":myfilters,
        "docs":docs,
        "Dtimes":Dtimes,    
    } 
    return render(request, "reservation/search.html",context)


