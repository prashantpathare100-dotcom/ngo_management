from decimal import Decimal
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from adpanel.models import AdminInfo
from .models import DonationMessage, Contact
from website.models import Donation
from website import models as web
from django.utils import timezone
import uuid
# ================= STATIC PAGES =================
def home(request):
    return render(request, "web/index.html")

def terms(request):
    return render(request, "web/terms.html")

def privacy(request):
    return render(request, "web/privacy.html")

def faq(request):
    return render(request, "web/faq.html")

def about(request):
    return render(request, "web/about.html")

def events(request):
    return render(request, "web/events.html")

def volunteers(request):
    return render(request, "web/volunteers.html")

def gallery(request):
    return render(request, "web/gallery.html")

def causes_programs(request):
    return render(request, "web/causes_programs.html")

def testimonials(request):
    return render(request, "web/testimonials.html")

def blog_news(request):
    return render(request, "web/blog_news.html")

def bna(request):
    return render(request, "web/b_n_a.html")

def bnb(request):
    return render(request, "web/b_n_b.html")

def bnc(request):
    return render(request, "web/b_n_c.html")


# ================= CONTACT PAGE =================
def contact(request):
    data = AdminInfo.objects.all()
    return render(request, "web/contact.html", {"data": data})


def contact_submit(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
    return redirect("contact")


# ================= DONATE PAGE =================
def donate(request):
    return render(request, "web/donate.html")


# ================= DONATION SAVE =================
def donation_s(request):
    txn_id = "TXN" + uuid.uuid4().hex[:14].upper()
    if request.method=="POST":
        
        save_data = web.Donation(

    name = request.POST.get("name"),
    email = request.POST.get("email"),
    phone = request.POST.get("phone"),
    cause = request.POST.get("cause"),
    cardno = (request.POST.get("cardno") or "").strip(),
    amount = request.POST.get("amount"),
    transaction_id=txn_id, 
    )
        save_data.save()
        print("SAVED SUCCESSFULLY ID =", save_data.id)
    
        return redirect(f"/donate/?success=1&amount={save_data.amount}&txn={txn_id}")
    
    return redirect("/donate/")




# ================= DONATION MESSAGE =================
def message_donate(request):
    if request.method == "POST":
        DonationMessage.objects.create(
            name=request.POST.get("name", "").strip(),
            email=request.POST.get("email", "").strip(),
            phone=request.POST.get("phone", "").strip(),
            subject=request.POST.get("subject", "").strip(),
            message=request.POST.get("message", "").strip(),
        )
    return redirect("donate_page")
