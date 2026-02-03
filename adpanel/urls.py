from django.urls import path
<<<<<<< HEAD

from adpanel import views

urlpatterns = [
    # path("donations/", views.admin_donations, name="admin_donations"),
    # path("donations/", views.admin_donations, name="admin_donations"),
    # path('donations/', views.donations_list, name='donations_list'),
    # path('donations/add/', views.donar_data, name='donar_data'),
    # path('donations/edit/<int:id>/', views.donation_edit, name='donation_edit'),
    # path('donations/delete/<int:id>/', views.donation_delete, name='donation_delete'),
    # path('donations/add/', views.donar_data, name='donation_add'),
]

=======
from . import views
>>>>>>> 200db6d5490057d1df43e554794e297daf680807
from .views import (
        volunteer_list,
        approve_volunteer,
        delete_volunteer,
        # gallery_list ,
        # delete_gallery,
        contact_list   
        
    )
    

urlpatterns = [
    # volunteers
    path('volunteers/', volunteer_list, name='volunteer_list' ),
    path('volunteer/approve/<int:id>/', approve_volunteer, name='approve_volunteer'),
    path('volunteer/delete/<int:id>/', delete_volunteer, name='delete_volunteer'),

    # gallery
    # gallery (donation list)
    # path('gallery/', gallery_list, name='gallery_list'),
    # path('gallery/delete/<int:id>/', delete_gallery, name='delete_gallery'),
<<<<<<< HEAD
    # path('gallery/', gallery_list, name='gallery_list'),
    # path('gallery/delete/<int:id>/', delete_gallery, name='delete_gallery'),
    # path("contact/", contact_list, name="contact"),
=======
    # gallery
    path('gallery/', gallery_list, name='gallery_list'),
    path('gallery/delete/<int:id>/', delete_gallery, name='delete_gallery'),
    path("contact/", contact_list, name="contact"),
>>>>>>> 200db6d5490057d1df43e554794e297daf680807

    # ✅ CONTACT 
    # path("contact/", views.contact_page),
    path("dashboard/contact/", contact_list, name="contact_list"),
    # path("dashboard/contact/delete/<int:id>/", contact_delete, name="contact_delete"),
    path("basic_info/", views.basic_info, name="basic_info"),
    path("save_profile/", views.save_profile, name="save_profile"),
    path("basic_info/delete/<int:id>/", views.delete_basic_info, name="delete_basic_info"),

    # testiomoinsal
    path("testionmals_info/", views.testionmals_info, name="testionmals_info"),

    
]