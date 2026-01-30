from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

# login
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# volunteers
from django.shortcuts import render
from volunteers.models import Volunteer
from django.shortcuts import render, redirect, get_object_or_404

# gallery

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from volunteers.models import Volunteer
from gallery.models import Donation




@login_required
def dashboard_view(request):

    # Temporary static totals (NO DB access)
    totals = {
        'total_donations': 0,
        'total_volunteers': 0,
        'total_events': 0,
    }

    sections = [
        {
            "title": "Testimonials Management",
            "icon": "fa-comments",
            "admin_can": [
                "Add testimonials",
                "Edit testimonials",
                "Delete testimonials",
            ],
            "fields": [
                "Name",
                "Image / Video",
                "Review",
                "Date",
            ],
        },
        {
            "title": "Contact Management",
            "icon": "fa-address-book",
            "admin_can": [
                "NGO address",
                "Phone number",
                "Email",
                "Social media links",
                "Google map location",
            ],
            "fields": [],
        },
        {
            "title": "Reports",
            "icon": "fa-chart-line",
            "admin_can": [
                "Generate donation reports",
                "Generate volunteer reports",
                "Generate event reports",
            ],
            "fields": [
                "Export PDF",
                "Export Excel",
            ],
        },
        {
            "title": "Profile & Login System",
            "icon": "fa-user-gear",
            "admin_can": [
                "Login",
                "Logout",
                "Change password",
                "Update profile",
            ],
            "fields": [],
        },
        {
            "title": "Role-Based Access",
            "icon": "fa-shield-halved",
            "admin_can": [
                "Super Admin – Full control",
                "Editor – Manage content only",
                "Finance – Donations & reports",
                "Volunteer Manager – Volunteers",
            ],
            "fields": [],
        },
    ]

    return render(request, "ad/dashboard.html", {
        "totals": totals,
        "sections": sections,
    })

# login 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_staff:
            login(request, user)
            return redirect("dashboard")   # dashboard
        else:
            messages.error(request, "Invalid admin credentials")

    return render(request, 'ad/login.html')

# # logout
# def logout_view(request):
#     logout(request)
#     return redirect('/login/')






def volunteer_list(request):
    volunteers = Volunteer.objects.all()  # 🔥 NO filter
    return render(
        request,
        'ad/volunteer_list.html',
        {'volunteers': volunteers}
    )
def approve_volunteer(request, id):
    volunteer = get_object_or_404(Volunteer, id=id)
    volunteer.is_approved = True
    volunteer.save()
    return redirect('volunteer_list')


def delete_volunteer(request, id):
    volunteer = get_object_or_404(Volunteer, id=id)
    volunteer.delete()
    return redirect('volunteer_list')


# gallery 


@login_required(login_url='/login/')
def gallery_list(request):
    items = Donation.objects.all().order_by('-created_at')
    return render(request, 'ad/gallery_list.html', {'items': items})



@login_required
def delete_gallery(request, id):
    donation = get_object_or_404(Donation, id=id)
    donation.delete()
    return redirect('gallery_list')

# contac
@login_required
def contact_list(request):
    contacts = Contact.objects.all().order_by("-created_at")
    return render(request, "ad/contact_list.html", {"contacts": contacts})
