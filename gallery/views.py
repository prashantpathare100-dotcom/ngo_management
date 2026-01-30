from django.shortcuts import render, redirect
from .models import Donation

def gallery_page(request):
    if request.method == "POST":
        print("🔥 POST RECEIVED 🔥")
        print(request.POST)

        Donation.objects.create(
            full_name=request.POST['full_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            amount=request.POST['amount'],
            cause=request.POST['cause'],
            message=request.POST.get('message', ''),
        )

        print("✅ SAVED TO DB")
        return redirect('gallery_page')

    return render(request, 'web/gallery.html')
