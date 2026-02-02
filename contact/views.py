from django.shortcuts import render, redirect
from django.http import JsonResponse   # ✅ CORRECT PLACE
from .models import ContactMessage, ContactHero, ContactInfo, GoogleMap, ContactTeam

def contact(request):
    print("==== CONTACT VIEW HIT ====")
    print("METHOD =", request.method)
    print("PATH =", request.path)

    hero = ContactHero.objects.first()
    info = ContactInfo.objects.first()
    map_data = GoogleMap.objects.first()
    team = ContactTeam.objects.all()

    if request.method == "POST":
        print("POST DATA =>", request.POST)

        ContactMessage.objects.create(
            name=request.POST.get('name'),      # ✅ correct
            email=request.POST.get('email'),    # ✅ correct
            subject=request.POST.get('subject'),
            message=request.POST.get('message'),
        )
        # AJAX response
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'success'})

        print("SAVED TO DB")
        return redirect('/contact/')

    context = {
        'hero': hero,
        'info': info,
        'map': map_data,
        'team': team
    }
    return render(request, 'web/contact.html', context)


def contact_list(request):
    messages = ContactMessage.objects.all().order_by('-created_at')
    print("DASHBOARD DATA =>", messages)
    return render(request, 'ad/contact_list.html', {'messages': messages})
