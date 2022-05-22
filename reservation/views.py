from django.http import QueryDict
from django.shortcuts import render
from .models import Doctors_profile
from .filters import DoctorsFilter

# from .models import Doctor, Major
# Create your views here.

# path("/docbymajor/<int:major_id>")   www.project.com/reservation/docbymajor/2
# major = Major.objects.get(id=major_id)
 #doctors = major.doctors.all()

def search(request):
    docs = Doctors_profile.objects.all()
    myfilters = DoctorsFilter(request.GET,queryset=docs)
    docs = myfilters.qs
    context = {
       # "doctors":doctors, 
        "myfilters":myfilters,
        "docs":docs,
    } 
    return render(request, "reservation/search.html")
