from django.shortcuts import render
from website import views 
# Create your views here.
def home(req):
    return render(req,"web/navbar.html")
