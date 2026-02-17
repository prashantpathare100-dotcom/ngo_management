from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.utils import timezone
from django.utils.timezone import localtime
from .models import ContactMessage

# ✅ Your models
from volunteers.models import Volunteer
from adpanel.models import AdminInfo, AdminInfop
from volunteers.models import Volunteer
from website.models import Donation, DonationMessage, Contact
from adpanel.models import AdminInfo, AdminInfop, ContactMessage
# ✅ PDF (ReportLab)
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import cm


# ------------------------------------------------------------
# LOGIN
# ------------------------------------------------------------
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


# ------------------------------------------------------------
# DASHBOARD
# ------------------------------------------------------------
@login_required
def dashboard(request):
    donation_qs = Donation.objects.all().order_by("-id")
    total_amount = donation_qs.aggregate(total=Sum("amount"))["total"] or 0

    context = {
        "donation": donation_qs[:10],          # recent donations table
        "donation_count": donation_qs.count(),
        "total_amount": total_amount,
        "volunteer_count": Volunteer.objects.count(),
        "enquiry_count": ContactMessage.objects.count(),
        "recent_donations": donation_qs[:4],
    }
    return render(request, "ad/dashboard.html", context)


# ------------------------------------------------------------
# CONTACTS (ADMIN)
# ------------------------------------------------------------
@login_required
def contact_list(request):
    # ✅ You had 2 different contact models earlier; use Contact (latest)
    contacts = Contact.objects.all().order_by("-id")
    return render(request, "ad/contact_list.html", {"contacts": contacts})


@login_required
def message_delete(request, id):
    msg = get_object_or_404(ContactMessage, id=id)
    msg.delete()
    return redirect("contact_list")


# ------------------------------------------------------------
# BASIC INFO (ADMININFO)
# ------------------------------------------------------------
@login_required
def basic_info(request):
    data = AdminInfo.objects.first()
    return render(request, "ad/basic_info.html", {"data": data})


@login_required
def save_basic_info(request):
    data = AdminInfo.objects.first()

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
            AdminInfo.objects.create(
                title=request.POST.get("title"),
                description=request.POST.get("description"),
                image=request.FILES.get("image"),
                photo=request.FILES.get("photo"),
                map_embed_url=request.POST.get("map_embed_url"),
                direction_link=request.POST.get("direction_link"),
                card_title=request.POST.get("card_title"),
                card_details=request.POST.get("card_details"),
            )

        return redirect("basic_info")

    return render(request, "ad/basic_info.html", {"data": data})


@login_required
def delete_basic_info(request, id):
    data = get_object_or_404(AdminInfo, id=id)
    data.delete()
    return redirect("basic_info")


@login_required
def profile(request):
    data = AdminInfo.objects.first()
    return render(request, "ad/profile.html", {"data": data})


@login_required
def testionmals_info(request):
    data = AdminInfo.objects.first()
    return render(request, "ad/testimonials.html", {"data": data})


# ------------------------------------------------------------
# VOLUNTEERS
# ------------------------------------------------------------
@login_required
def volunteer_list(request):
    volunteers = Volunteer.objects.all().order_by("-id")
    return render(request, "ad/volunteer_list.html", {"volunteers": volunteers})


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

from website import models as web
@login_required
def donar(request):
    donation_qs = web.Donation.objects.all().order_by("-id")
    total_amount = donation_qs.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request,"ad/donar_l.html",{"donation": donation_qs,"total_amount": total_amount})


# ================= DELETE =================
@login_required
def donation_delete(request, id):
    d = get_object_or_404(Donation, id=id)
    d.delete()
    return redirect("donar")


# ================= RECEIPT PDF =================
@login_required
def donation_receipt_pdf(request, pk):
    d = get_object_or_404(Donation, pk=pk)

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="receipt_{d.id}.pdf"'

    c = canvas.Canvas(response, pagesize=A4)
    w, h = A4

    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, h - 60, "Donation Receipt")

    c.setFont("Helvetica", 12)
    c.drawString(50, h - 100, f"Name: {d.name}")
    c.drawString(50, h - 120, f"Email: {d.email}")
    c.drawString(50, h - 140, f"Phone: {d.phone}")
    c.drawString(50, h - 160, f"Amount: ₹{d.amount}")
    c.drawString(50, h - 180, f"Cause: {d.cause}")

    dt = localtime(d.created_at).strftime("%d-%m-%Y %H:%M")
    c.drawString(50, h - 200, f"Date: {dt}")

    c.showPage()
    c.save()
    return response


@login_required
def donations_report_pdf(request):
    donations = Donation.objects.all().order_by("-id")
    total_amount = donations.aggregate(total=Sum("amount"))["total"] or 0
    total_count = donations.count()

    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="donations_report.pdf"'

    c = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    # ===== Header =====
    c.setFont("Helvetica-Bold", 18)
    c.drawString(2 * cm, height - 2 * cm, "Donations Report")

    c.setFont("Helvetica", 11)
    c.drawString(2 * cm, height - 3 * cm, f"Total Donations: {total_count}")
    c.drawString(2 * cm, height - 3.7 * cm, f"Total Amount: ₹{total_amount}")

    # Line
    c.setStrokeColor(colors.grey)
    c.line(2 * cm, height - 4.2 * cm, width - 2 * cm, height - 4.2 * cm)

    # ===== Table Header =====
    y = height - 5 * cm
    c.setFont("Helvetica-Bold", 10)
    c.drawString(2 * cm, y, "Name")
    c.drawString(7 * cm, y, "Amount")
    c.drawString(10 * cm, y, "Cause")
    c.drawString(14 * cm, y, "Date")

    c.setFont("Helvetica", 9)
    y -= 0.8 * cm

    # ===== Table Rows =====
    for d in donations:
        if y < 2 * cm:
            c.showPage()
            y = height - 2 * cm

        date_str = localtime(d.created_at).strftime("%d-%m-%Y")

        c.drawString(2 * cm, y, d.name[:20])
        c.drawString(7 * cm, y, f"₹{d.amount}")
        c.drawString(10 * cm, y, d.cause[:20])
        c.drawString(14 * cm, y, date_str)

        y -= 0.6 * cm

    c.save()
    return response
# ------------------------------------------------------------
# PROFILE (AdminInfop) - SAVE / DELETE
# ------------------------------------------------------------
@login_required
def save_profile(request):
    if request.method == "POST":
        AdminInfop.objects.create(
            name=request.POST.get("name", "").strip(),
            mobile=request.POST.get("mobile", "").strip(),
            email=request.POST.get("email", "").strip(),
            gender=request.POST.get("gender", "").strip(),
            password=request.POST.get("password", "").strip(),
            facebook=request.POST.get("facebook", "").strip(),
            instagram=request.POST.get("instagram", "").strip(),
            linkedin=request.POST.get("linkdin", "").strip(),
            whatsapp=request.POST.get("watssap", "").strip(),
            profile=request.FILES.get("profile"),
            logo=request.FILES.get("logo"),
        )
        return redirect("donar")  # किंवा तुझ्या profile list page ला redirect कर

    return redirect("donar")


@login_required
def profile_delete(request, id):
    obj = get_object_or_404(AdminInfop, id=id)
    obj.delete()
    return redirect("donar")


# ------------------------------------------------------------
# EVENTS PAGE (ADMIN)
# ------------------------------------------------------------
@login_required
def events_page(request):
    return render(request, "ad/event_list.html")



# ------------------------------------------------------------
@login_required
def message_list(request):
    msgs = DonationMessage.objects.all().order_by("-id")
    return render(request, "ad/message_list.html", {"messages": msgs})


@login_required
def donation_message_delete(request, id):
    msg = get_object_or_404(DonationMessage, id=id)
    msg.delete()
    return redirect("message_list")
