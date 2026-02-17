from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from adpanel import views as ad
from website import views as ui


urlpatterns = [
    # ===================== WEBSITE PAGES =====================
    path("", ui.home, name="home"),
    path("terms/", ui.terms, name="terms"),
    path("privacy/", ui.privacy, name="privacy"),
    path("faq/", ui.faq, name="faq"),
    path("contact/", ui.contact, name="contact"),
    path("about/", ui.about, name="about"),
    path("events/", ui.events, name="events"),
    path("gallery/", ui.gallery, name="gallery"),
    path("causes_programs/", ui.causes_programs, name="causes_programs"),
    path("testimonials/", ui.testimonials, name="testimonials"),
    path("blog_news/", ui.blog_news, name="blog_news"),
    path("bna/", ui.bna, name="bna"),
    path("bnb/", ui.bnb, name="bnb"),
    path("bnc/", ui.bnc, name="bnc"),

    # Donate + forms
    path("donate/", ui.donate, name="donate"),
    path("donation_s/", ui.donation_s, name="donation_s"),               # donation save (simple)
    path("message_donate/", ui.message_donate, name="message_donate"),
    # ⚠️ donation_submit (ContactMessage वाला) जर तू clean website/views.py वापरत असशील तर हा URL काढ.
    # path("donation/submit/", ui.donation_submit, name="donation_submit"),

    # Volunteers (website + app)
    path("volunteer/", ui.volunteers, name="volunteer_page"),
    path("volunteers/", include(("volunteers.urls", "volunteers"), namespace="volunteers")),

    # ===================== ADMIN AUTH =====================
    path("adminn/", ad.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page=reverse_lazy("login")), name="logout"),

    # ===================== ADMIN PAGES =====================
    path("adminn/dashboard/", ad.dashboard, name="dashboard"),  # ✅ clean views मधला dashboard
    path("donations/", ad.donar, name="donar"),                 # ✅ donation list
    path("donations/delete/<int:id>/", ad.donation_delete, name="donation_delete"),
    path("donation/<int:pk>/receipt/", ad.donation_receipt_pdf, name="donation_receipt_pdf"),
    path("dashboard/report/", ad.donations_report_pdf, name="donations_report_pdf"),

    # Volunteers admin actions
    path("admin/volunteers/", ad.volunteer_list, name="volunteer_list"),
    path("admin/volunteers/approve/<int:id>/", ad.approve_volunteer, name="approve_volunteer"),
    path("admin/volunteers/delete/<int:id>/", ad.delete_volunteer, name="delete_volunteer"),

    # Basic info / profile
    path("basic_info/", ad.basic_info, name="basic_info"),
    path("basic_info/save/", ad.save_basic_info, name="save_basic_info"),
    path("basic_info/delete/<int:id>/", ad.delete_basic_info, name="delete_basic_info"),
    path("profile/", ad.profile, name="profile"),

    # Messages / contact admin
    path("messages/", ad.message_list, name="message_list"),
    path("messages/delete/<int:id>/", ad.donation_message_delete, name="donation_message_delete"),
    path("admin/contacts/", ad.contact_list, name="contact_list"),
    path("admin/contacts/delete/<int:id>/", ad.message_delete, name="message_delete"),
    path("adminn/donations/", ad.donar, name="donar"),
    # Events admin page
    path("admin/events/", ad.events_page, name="events_page"),
    path("adminn/donation/<int:pk>/receipt/", ad.donation_receipt_pdf, name="donation_receipt_pdf"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   



   
    
