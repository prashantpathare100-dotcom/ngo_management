from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Donation, GalleryItem



# ---------------- Donation part (as it is) ----------------
def gallery_page(request):
    if request.method == "POST":
        Donation.objects.create(
            full_name=request.POST.get("full_name", "").strip(),
            email=request.POST.get("email", "").strip(),
            phone=request.POST.get("phone", "").strip(),
            amount=request.POST.get("amount") or 0,
            cause=request.POST.get("cause", "").strip(),
            message=request.POST.get("message", "").strip(),
        )
        return redirect("gallery_list")

    donation = Donation.objects.all().order_by("-id")
    return render(request, "ad/gallery_list.html", {"donation": donation})


def gallery_list(request):
    donation = Donation.objects.all().order_by("-id")
    return render(request, "ad/gallery_list.html", {"donation": donation})


def delete_gallery(request, id):
    obj = get_object_or_404(Donation, id=id)
    obj.delete()
    return redirect("gallery_list")


