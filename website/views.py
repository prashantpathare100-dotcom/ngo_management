from django.shortcuts import render
from website import views 
# Create your views here.
def home(req):
    return render(req,"web/index.html")

def terms(req):
    return render(req,"web/terms.html")

def privacy(req):
    return render(req,"web/privacy.html")

def faq(req):
    return render(req,"web/faq.html")

def contact(req):
    return render(req,"web/contact.html")
def donate(req):
    return render(req,"web/donate.html")
    
def about(req):
    return render(req,"web/about.html")

def events(req):
    return render(req,"web/events.html")

def volunteers(req):
    return render(req,"web/volunteers.html")

def gallery(req):
    return render(req,"web/gallery.html")

def causes_programs(req):
    return render(req,"web/causes_programs.html")

def testimonials(req):
    return render(req,"web/testimonials.html")

def blog_news(req):
    return render(req,"web/blog_news.html")

def bna(req):
    return render(req,"web/b_n_a.html")

def bnb(req):
    return render(req,"web/b_n_b.html")

def bnc(req):
    return render(req,"web/b_n_c.html")



from django.shortcuts import redirect
from django.contrib import messages
from website.models import Donation, ContactMessage

def contact_submit(request):
    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        messages.success(request, "Message sent successfully!")
        return redirect(request.META.get("HTTP_REFERER", "/"))
    return redirect("/")



def donation_submit(request):
    if request.method == "POST":
        Donation.objects.create(
            cause_id=request.POST.get("cause_id") or None,
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            pan=request.POST.get("pan"),
            amount=int(request.POST.get("amount") or 0),
        )
        messages.success(request, "Donation submitted successfully!")
        return redirect("donate_page")   # website donate page
    return redirect("/")

def donar_list(request):
    donations = Donation.objects.all().order_by("-id")
    return render(request, "ad/donar_list.html", {"donations": donations})

