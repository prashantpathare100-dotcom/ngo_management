from django.shortcuts import render, redirect
from .models import Volunteer
def volunteers_page(request):
    if request.method == "POST":
        print("FORM SUBMITTED")
        Volunteer.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            age=request.POST.get("age"),
            volunteer_type=request.POST.get("volunteer_type"),
            message=request.POST.get("message"),
        )
        print("RECORD SAVED")
        return redirect("website_volunteers")

    return render(request, "web/volunteers.html")

def volunteer_list(request):
   return render(request, "ad/volunteer_list.html")
