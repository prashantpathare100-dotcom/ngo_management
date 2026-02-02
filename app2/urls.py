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

urlpatterns = [
    path('admin/', admin.site.urls),
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
    path('volunteers/',ui.volunteers),
    path('volunteers/', include('volunteers.urls')),
    path('adminn/', login_view, name='login'),
    path('adminn/dashboard/', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login2'),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("login")), name="logout"),
    
    path("contact/submit/", ui.contact_submit, name="contact_submit"),
    path("donation/submit/", ui.donation_submit, name="donation_submit"),
    path("donations/", ui.donar_list, name="donations_list"),
    # admin/dashboard lists
    

    path("donations/delete/<int:id>/", ad.donation_delete, name="donation_delete"),
    path("messages/delete/<int:id>/", ad.message_delete, name="message_delete"),
    path("donation-submit/", ui.donation_submit, name="donation_submit"),
]






    
    
  