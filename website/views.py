from decimal import Decimal
from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.db.models import Sum
from adpanel.models import ContactMessage, AdminInfo
from .models import Donation, DonationMessage, Contact


# Create your views here.
def home(req):
    return render(req, "web/index.html")

def terms(req):
    return render(req, "web/terms.html")

def privacy(req):
    return render(req, "web/privacy.html")

def faq(req):
    return render(req, "web/faq.html")

def contact(req):
    data = AdminInfo.objects.all()
    return render(req, "web/contact.html", {"data": data})

def donate(req):
    return render(req, "web/donate.html")

def about(req):
    return render(req, "web/about.html")

def events(req):
    return render(req, "web/events.html")

def volunteers(req):
    return render(req, "web/volunteers.html")

def gallery(req):
    return render(req, "web/gallery.html")

def causes_programs(req):
    return render(req, "web/causes_programs.html")

def testimonials(req):
    return render(req, "web/testimonials.html")

def blog_news(req):
    return render(req, "web/blog_news.html")

def bna(req):
    return render(req, "web/b_n_a.html")

def bnb(req):
    return render(req, "web/b_n_b.html")

def bnc(req):
    return render(req, "web/b_n_c.html")


# ✅ kept only ONE donation_submit (ContactMessage save)
def donation_submit(req):
    if req.method != "POST":
        return redirect("/donate/")

    name = (req.POST.get("name") or "").strip()
    email = (req.POST.get("email") or "").strip()
    phone = (req.POST.get("phone") or "").strip()
    pan = (req.POST.get("pan") or "").strip()
    cause_id = (req.POST.get("cause_id") or "").strip()

    amount_str = (req.POST.get("amount") or "").strip()
    if not amount_str:
        return HttpResponseBadRequest("Amount is required")

    try:
        amount = Decimal(amount_str)
    except Exception:
        return HttpResponseBadRequest("Invalid amount")

    ContactMessage.objects.create(
        name=name,
        email=email,
        phone=phone,
        subject="Donation",
        amount=amount,
        message=f"PAN: {pan}, Cause: {cause_id}",
    )
    return redirect("/donate/")


def contact_submit(req):
    if req.method == "POST":
        ContactMessage.objects.create(
            name=req.POST.get("name"),
            email=req.POST.get("email"),
            subject=req.POST.get("subject"),
            message=req.POST.get("message"),
        )
    return redirect("/contact/")

from django.contrib import messages


def donation_s(req):
    if req.method == "POST":
        Donation.objects.create(
            name=req.POST.get("name"),
            email=req.POST.get("email"),
            phone=req.POST.get("phone"),
            cardno=req.POST.get("cardno"),
            amount=req.POST.get("amount"),
            cause=req.POST.get("cause"),
        )


        return redirect("donate_page")




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


def contact_page(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
    return redirect("contact")
