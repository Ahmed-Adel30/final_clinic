from django.shortcuts import render
# from .models import Doctor, Major
# Create your views here.

# path("/docbymajor/<int:major_id>")   www.project.com/reservation/docbymajor/2
def get_doctors_by_major(request, major_id):
    major = Major.objects.get(id=major_id)
    doctors = major.doctors.all()

    context = {
        "doctors":doctors
    }
    return render(request, "temp.html", context)
