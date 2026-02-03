from django.shortcuts import render, redirect, get_object_or_404
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
        return redirect("website_volunteers")  # तुमचा url name

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
        return redirect("/volunteers/")  # किंवा redirect("website_volunteers")

    # ✅ IMPORTANT: GET request आला तरी HttpResponse return करणे आवश्यक आहे
    return render(request, "ad/volunteer_list.html")


def approve_volunteer(request, id):
    volunteer = get_object_or_404(Volunteer, id=id)
    volunteer.is_approved = True
    volunteer.save()
    return redirect("volunteer_list")


def delete_volunteer(request, id):
    volunteer = get_object_or_404(Volunteer, id=id)
    volunteer.delete()
    return redirect("volunteer_list")
