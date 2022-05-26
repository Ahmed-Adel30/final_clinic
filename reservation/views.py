from django.http import QueryDict
from django.shortcuts import redirect, render
from django.urls import is_valid_path

from .models import Doc_time, Doctors_profile
from .filters import DoctorsFilter
from .forms import Doc_timeForm




def search(request):
    docs = Doctors_profile.objects.all()
    Dtimes = Doc_time.objects.all()
    form = Doc_timeForm()
    myfilters = DoctorsFilter(request.GET,queryset=docs)
    docs = myfilters.qs
    context = {
        "myfilters":myfilters,
        "docs":docs,
        "Dtimes":Dtimes, 
        "form":form   
    } 
    if request.method =='POST':
        form= Doc_timeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("credit_card")
        
    return render(request, "reservation/search.html",context)


