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