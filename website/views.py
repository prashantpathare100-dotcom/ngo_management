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