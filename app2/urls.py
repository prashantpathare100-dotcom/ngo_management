"""
URL configuration for app2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include, reverse_lazy
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from adpanel import views as ad
from website import views as ui
from adpanel.views import login_view, dashboard_view

from django.urls import path , include

from django.contrib.auth.views import LogoutView  
from adpanel.views import dashboard_view , login_view  
from website import views as ui
from django.urls import reverse_lazy
from adpanel.views import contact_list
from django.conf import settings
from django.conf.urls.static import static


# contact

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', ui.home, name='home'),
    path('terms/', ui.terms, name='terms'),
    path('privacy/', ui.privacy, name='privacy'),
    path('faq/', ui.faq, name='faq'),
    path('contact/', ui.contact, name='contact'),
    path('about/', ui.about, name='about'),
    path('events/', ui.events, name='events'),
    path('gallery/', ui.gallery, name='gallery'),
    path('causes_programs/', ui.causes_programs, name='causes_programs'),
    path('testimonials/', ui.testimonials, name='testimonials'),
    path('blog_news/', ui.blog_news, name='blog_news'),
    path('bna/', ui.bna, name='bna'),
    path('bnb/', ui.bnb, name='bnb'),
    path('bnc/', ui.bnc, name='bnc'),  
    path('donate/', ui.donate, name='donate_page'),
    path('volunteer/',ui.volunteers),
    path("volunteers/", include(("volunteers.urls", "volunteers"), namespace="volunteers")),
    path('adminn/', login_view, name='login'),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("login")), name="logout"),
    path("donation/submit/", ui.donation_submit, name="donation_submit"),
    path("donation_s/", ui.donation_s, name="donation_s"),
    path('causes_programs/',ui.causes_programs),
    path('testimonials/',ui.testimonials),
    path('blog_news/',ui.blog_news),
    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("login")),
        name="logout"
    ),
    path("adminn/dashboard/", ad.dashboard_view, name="dashboard"),
     path('volunteer/', include('volunteers.urls')),

    path('dashboard/', include('adpanel.urls')),   
    path("", include("gallery.urls")),
    path("donations/delete/<int:id>/", ad.donation_delete, name="donation_delete"),
        path("profile/delete/<int:id>/", ad.profile_delete, name="profile_delete"),
    path('basic_info/',ad.basic_info),

    # path('profile/',ad.profile),
    # path("save_profile/",ad.save_profile),
    path("gallery_list/", ad.gallery_list, name="gallery_list"),
    path("donation-submit/", ui.donation_submit, name="donation_submit"),
    path('donations/',ad.donar,name="donations"),
    # testimoinals
    path("testionmals_info/",ad.testionmals_info),
    path("volunteers/", ad.volunteer_list, name="volunteers"),
    path("donation/<int:pk>/receipt/", ad.donation_receipt_pdf, name="donation_receipt_pdf"),
    path("messages/", ad.message_list, name="message_list"),
    path("messages/delete/<int:id>/", ad.donation_message_delete, name="donation_message_delete"),

    path("event/", ad.events_page, name="events_page"),
    path("message_donate/", ui.message_donate, name="message_donate"),
    path("messages/", ad.message_list, name="message_list"),
    path("contcontact_page/", ui.contact_page, name="contact_page"),
    path("dashboard/contact/", ad.dashboard_contact, name="dashboard_contact"),
    path('adminn/dashboard/', ad.dashboard_view, name='dashboard'),
    path("dashboard/report/", ad.donations_report_pdf, name="donations_report_pdf"),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



   


    
    
  