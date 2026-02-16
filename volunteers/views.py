from django.shortcuts import render, redirect
from .models import Volunteer

from .models import Volunteer
def volunteers_page(request):
    if request.method == "POST":
        Volunteer.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            age=request.POST.get("age"),
            volunteer_type=request.POST.get("volunteer_type"),
            message=request.POST.get("message"),
        )
        return redirect("volunteer")  # 👈 SAME PAGE

    return render(request, "web/volunteers.html")




def website_volunteer_submit(request):
    if request.method == "POST":
        Volunteer.objects.create(
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            age=request.POST.get("age"),
            volunteer_type=request.POST.get("volunteer_type"),
            message=request.POST.get("message"),
        )
        return redirect("/volunteer/")