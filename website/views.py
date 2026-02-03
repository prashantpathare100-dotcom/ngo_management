from django.shortcuts import render
from website import views 
from django.shortcuts import redirect
from adpanel.models import ContactMessage
from .import models
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
    data = models.AdminInfo.Objects.all()
    return render(req,"web/contact.html",{"data":data})
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


def donation_submit(request):

    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )



def contact_submit(request):

    if request.method == "POST":
        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )

    return redirect("contact")
