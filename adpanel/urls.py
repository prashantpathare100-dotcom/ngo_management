from django.urls import path
from . import views
from .views import (
        volunteer_list,
        approve_volunteer,
        delete_volunteer,
        gallery_list ,
        delete_gallery,
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
    # gallery
    path('gallery/', gallery_list, name='gallery_list'),
    path('gallery/delete/<int:id>/', delete_gallery, name='delete_gallery'),
    path("contact/", contact_list, name="contact"),

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