from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from volunteers.models import Volunteer


from adpanel import models
from .models import ContactMessage


# ================= LOGIN =================
def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "ad/login.html", {"error": "Invalid Login"})

    return render(request, "ad/login.html")


# ================= DASHBOARD =================
@login_required
<<<<<<< HEAD
def donations_list(request):
    donations = Donation.objects.all().order_by('-created_at')
    return render(request, 'donate_list.html', {'donations': donations})
=======
def dashboard_view(request):
    return render(request, "ad/dashboard.html")


# ================= CONTACT LIST =================
@login_required
def contact_list(request):
    contacts = ContactMessage.objects.all().order_by("-id")
    return render(request, "ad/contact_list.html", {
        "messages": contacts
    })
>>>>>>> 200db6d5490057d1df43e554794e297daf680807


# ================= CONTACT PAGE =================
def contact_page(request):

    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        return redirect("contact")

    data = models.AdminInfo.objects.all()
    return render(request, "web/contact.html", {"data": data})


# ================= BASIC INFO =================
def basic_info(request):
    data = models.AdminInfo.objects.first()
    return render(request, "ad/basic_info.html", {"data": data})


# ================= SAVE PROFILE =================
def save_profile(request):

    data = models.AdminInfo.objects.first()

    if request.method == "POST":

        if data:
            data.title = request.POST.get("title")
            data.description = request.POST.get("description")

            if request.FILES.get("image"):
                data.image = request.FILES.get("image")

            if request.FILES.get("photo"):
                data.photo = request.FILES.get("photo")

            data.map_embed_url = request.POST.get("map_embed_url")
            data.direction_link = request.POST.get("direction_link")
            data.card_title = request.POST.get("card_title")
            data.card_details = request.POST.get("card_details")

            data.save()

        else:
            models.AdminInfo.objects.create(
                title=request.POST.get("title"),
                description=request.POST.get("description"),
                image=request.FILES.get("image"),
                photo=request.FILES.get("photo"),
                map_embed_url=request.POST.get("map_embed_url"),
                direction_link=request.POST.get("direction_link"),
                card_title=request.POST.get("card_title"),
                card_details=request.POST.get("card_details"),
            )

        return redirect('basic_info')

    return render(request, "ad/basic_info.html", {"data": data})


# ================= PROFILE =================
def profile(request):
    return render(request, "ad/profile.html")


# ================= DELETE BASIC INFO =================
@login_required
def delete_basic_info(request, id):
    data = models.AdminInfo.objects.get(id=id)
    data.delete()
    return redirect("basic_info")
@login_required
def volunteer_list(request):
    volunteers = Volunteer.objects.all().order_by("-id")
    return render(request, "ad/volunteer_list.html", {
        "volunteers": volunteers
    })

@login_required
def approve_volunteer(request, id):
    volunteer = get_object_or_404(Volunteer, id=id)

    volunteer.status = "approved"   # ⚠ field name तुमच्या model प्रमाणे change करा
    volunteer.save()

    return redirect("volunteer_list")
@login_required
def delete_volunteer(request, id):
    volunteer = get_object_or_404(Volunteer, id=id)
    volunteer.delete()
    return redirect("volunteer_list")   
@login_required
def gallery_list(request):
    gallery = Donation.objects.all().order_by("-id")

    return render(request, "ad/gallery_list.html", {
        "gallery": gallery
    })
@login_required
def delete_gallery(request, id):
    gallery_item = get_object_or_404(Donation, id=id)
    gallery_item.delete()
    return redirect("gallery_list")


def testionmals_info(request):
    data = models.AdminInfo.objects.first()
    return render(request, "ad/testimonials.html", {"data": data})
def volunteer_submit(request):
    return redirect("volunteer_list")

@login_required
def donation_delete(request, id):
<<<<<<< HEAD
    d = get_object_or_404(Donation, id=id)
    d.delete()
    messages.success(request, "Donation deleted!")
    return redirect("donations_list")

def message_delete(request, id):
    m = get_object_or_404(ContactMessage, id=id)
    m.delete()
    messages.success(request, "Message deleted!")
    return redirect("messages_list")


def delete_gallery(request, id):
=======
>>>>>>> 200db6d5490057d1df43e554794e297daf680807
    donation = get_object_or_404(Donation, id=id)
    donation.delete()
    return redirect("gallery_list")

<<<<<<< HEAD
# contac
@login_required
def contact_list(request):
    contacts = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'ad/contact_list.html', {'contacts': contacts})

def donar_list(request):
    donations = Donation.objects.all().order_by('-id')
    return render(request, 'ad/donar_list.html', {'donations': donations})
=======

def message_delete(request, id):
    message = get_object_or_404(ContactMessage, id=id)
    message.delete()
    return redirect("contact_list")   
>>>>>>> 200db6d5490057d1df43e554794e297daf680807
