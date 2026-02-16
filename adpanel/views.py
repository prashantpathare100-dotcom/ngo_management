from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from volunteers.models import Volunteer
from gallery.models import Donation
from adpanel.models import AdminInfop
from adpanel import models
from .models import ContactMessage
from django.db.models import Sum
from gallery.models import Donation  
from reportlab.lib.units import cm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from django.utils.timezone import localtime
# ================= LOGIN =================
def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )
        if user:
            login(request, user)
            return redirect("dashboard")
        return render(request, "ad/login.html", {"error": "Invalid Login"})
    return render(request, "ad/login.html")


# ================= DASHBOARD =================
@login_required
def dashboard_view(request):
    donation_qs = Donation.objects.all().order_by("-id")

    context = {
        "donation": donation_qs[:10],  # recent donations table
        "donation_count": donation_qs.count(),
        "total_amount": donation_qs.aggregate(total=Sum("amount"))["total"] or 0,
        "volunteer_count": Volunteer.objects.count(),
        "enquiry_count": ContactMessage.objects.count(),
        "recent_donations": donation_qs[:4],
    }
    return render(request, "ad/dashboard.html", context)


# ================= CONTACT LIST =================
@login_required
def contact_list(request):
    contacts = ContactMessage.objects.all().order_by("-id")
    return render(request, "ad/contact_list.html", {
        "messages": contacts
    })


# ================= CONTACT PAGE =================



    
# ================= BASIC INFO =================
def basic_info(request):
    data =models.AdminInfo.objects.first()
    return render(request, "ad/basic_info.html", {"data": data})


# ================= SAVE PROFILE =================
def save_basic_info(request):

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
                # photo=request.FILES.get("photo"),
                # map_embed_url=request.POST.get("map_embed_url"),
                # direction_link=request.POST.get("direction_link"),
                card_title=request.POST.get("card_title"),
                card_details=request.POST.get("card_details"),
                
            )

        return redirect('basic_info')
   

    return render(request, "ad/basic_info.html", {"data": data})


# ================= PROFILE =================
def profile(request):
    data = models.AdminInfo.objects.first() 
    return render(request, "ad/profile.html ",{"data": data})

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

    volunteer.status = "approved"   
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
    donation = get_object_or_404(Donation, id=id)
    donation.delete()
    return redirect("gallery_list")


def message_delete(request, id):
    message = get_object_or_404(ContactMessage, id=id)
    message.delete()
    return redirect("contact_list")


def donar_list(req):
    profile = models.AdminInfop.objects.all()
    return render(req,"ad/donar_list.html")


def save_profile(req):
    if req.method == "POST":
        save_data =models.AdminInfop(
    
        name   = req.POST.get('name', '').strip(),
        mobile = req.POST.get('mobile', '').strip(),
        email  = req.POST.get('email', '').strip(),
        gender = req.POST.get('gender', '').strip(),
        password = req.POST.get('password', '').strip(),
        facebook  = req.POST.get('facebook', '').strip(),
        instagram = req.POST.get('instagram', '').strip(),
        linkedin   = req.POST.get('linkdin', '').strip(),
        whatsapp   = req.POST.get('watssap', '').strip(),
        profile = req.FILES.get('profile', None),
        logo = req.FILES.get('logo'),
    )

    save_data.save()
    profilel = models.AdminInfop.objects.all()
    return render(req,"ad/donar_l.html",{"profilel":profilel})

def profile_delete(request, id):
    obj = get_object_or_404(models.AdminInfop, id=id)   
    obj.delete()
    profile = models.AdminInfop.objects.all()
    return render(request,"ad/donar_l.html",{"profile":profile})

def donation(req):
    donations = ContactMessage.objects.filter(subject="Donation").order_by("-id")
    return render(req, "ad/donar_l.html", {"donations": donations})

def donation_list(req):
    donations = ContactMessage.objects.filter(subject="Donation").order_by("-id")
    return render(req, "ad/donar_l.html", {"donations": donations})

from django.shortcuts import render
from website.models import Donation   



def donar(req):
    donation = Donation.objects.all().order_by("-id")
    return render(req, "ad/donar_l.html", {"donation": donation})
def donation_delete(request, id):
    donation = get_object_or_404(Donation, id=id)
    donation.delete()
    return redirect(donar)

def volunteer_list(request):
    volunteers = Volunteer.objects.all()
    return render(request, "ad/volunteer_list.html", {
        "volunteers": volunteers
    })



def donation_delete(request, id):
    d = get_object_or_404(Donation, id=id)
    d.delete()
    return redirect("dashboard") 






@login_required
def donation_receipt_pdf(request, pk):
    d = get_object_or_404(Donation, pk=pk)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="receipt_{d.id}.pdf"'

    c = canvas.Canvas(response, pagesize=A4)
    w, h = A4

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, h - 60, "Donation Receipt")
    c.line(50, h - 70, w - 50, h - 70)

    c.setFont("Helvetica", 11)
    c.drawString(50, h - 100, f"Donor: {d.name}")
    c.drawString(50, h - 120, f"Email: {d.email}")
    c.drawString(50, h - 140, f"Phone: {d.phone}")
    c.drawString(50, h - 160, f"Amount: ₹{d.amount}")
    c.drawString(50, h - 180, f"Cause: {d.cause}")

    dt = localtime(d.created_at).strftime("%d-%m-%Y %H:%M")
    c.drawString(50, h - 200, f"Date: {dt}")

    c.showPage()
    c.save()
    return response


def events_page(req):

    return render(req,"ad/event_list.html")

from website.models import DonationMessage




@login_required
def message_list(request):
    msgs = DonationMessage.objects.all().order_by("-id")
    return render(request, "ad/message_list.html", {"messages": msgs})

from website.models import Contact

def dashboard_contact(request):
    contacts = Contact.objects.all().order_by("-id")
    print("CONTACTS COUNT:", contacts.count())
    return render(request, "ad/contact_list.html", {"contacts": contacts})

def donation_message_delete(request, id):
    msg = get_object_or_404(DonationMessage, id=id)
    msg.delete()
    return redirect("message_list")

def donations_report_pdf(request):
    qs = Donation.objects.all().order_by("-id")

    total_amount = qs.aggregate(total=Sum("amount"))["total"] or 0
    total_count = qs.count()

   
    rows = qs[:100]

    # PDF response
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="donations_report.pdf"'

    c = canvas.Canvas(response, pagesize=A4)
    w, h = A4

    # Header
    c.setFont("Helvetica-Bold", 18)
    c.drawString(2 * cm, h - 2.2 * cm, "Donations Report")

    c.setFont("Helvetica", 10)
    c.setFillColor(colors.grey)
    c.drawString(2 * cm, h - 2.9 * cm, f"Generated: {timezone.localtime().strftime('%d-%m-%Y %I:%M %p')}")
    c.setFillColor(colors.black)

    c.setStrokeColor(colors.lightgrey)
    c.line(2 * cm, h - 3.2 * cm, w - 2 * cm, h - 3.2 * cm)

    # Summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(2 * cm, h - 4.1 * cm, "Summary")

    c.setFont("Helvetica", 11)
    c.drawString(2 * cm, h - 4.8 * cm, f"Total Transactions: {total_count}")
    c.drawString(2 * cm, h - 5.5 * cm, f"Total Amount: \u20B9{total_amount}")

    # Table header
    y = h - 6.5 * cm
    c.setFont("Helvetica-Bold", 10)
    c.setFillColor(colors.white)
    c.setStrokeColor(colors.darkgrey)
    c.setFillColor(colors.black)

    # Columns positions
    x_name = 2 * cm
    x_amount = 9.5 * cm
    x_cause = 12.5 * cm
    x_date = 17.0 * cm

    c.setFont("Helvetica-Bold", 10)
    c.drawString(x_name, y, "Name")
    c.drawString(x_amount, y, "Amount")
    c.drawString(x_cause, y, "Cause")
    c.drawString(x_date, y, "Date")

    c.setStrokeColor(colors.lightgrey)
    c.line(2 * cm, y - 3, w - 2 * cm, y - 3)

    # Rows
    c.setFont("Helvetica", 9)
    y -= 0.7 * cm

    for d in rows:
        if y < 2.2 * cm:
            c.showPage()
            y = h - 2.2 * cm
            c.setFont("Helvetica-Bold", 10)
            c.drawString(x_name, y, "Name")
            c.drawString(x_amount, y, "Amount")
            c.drawString(x_cause, y, "Cause")
            c.drawString(x_date, y, "Date")
            c.setStrokeColor(colors.lightgrey)
            c.line(2 * cm, y - 3, w - 2 * cm, y - 3)
            c.setFont("Helvetica", 9)
            y -= 0.7 * cm

        name = (d.name or "")[:28]
        cause = (getattr(d, "cause", "") or "")[:20]
        dt = ""
        if getattr(d, "created_at", None):
            dt = timezone.localtime(d.created_at).strftime("%d-%m-%Y")

        c.drawString(x_name, y, name)
        c.drawRightString(x_amount + 2.0 * cm, y, f"\u20B9{d.amount}")
        c.drawString(x_cause, y, cause)
        c.drawString(x_date, y, dt)

        y -= 0.55 * cm

    # Footer
    c.setFont("Helvetica-Oblique", 9)
    c.setFillColor(colors.grey)
    c.drawString(2 * cm, 1.5 * cm, "Computer-generated report")
    c.save()

    return response
def donar(request):
    donation = Donation.objects.all().order_by("-id")

    total_amount = donation.aggregate(
        total=Sum("amount")
    )["total"] or 0

    context = {
        "donation": donation,
        "total_amount": total_amount,
    }

    return render(request, "ad/donar_l.html", context)


