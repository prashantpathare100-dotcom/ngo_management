from django.urls import path

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

from .views import (
        volunteer_list,
        approve_volunteer,
        delete_volunteer,
        # gallery_list ,
        # delete_gallery,
        contact_list   
        
    )

urlpatterns = [
        path('volunteers/', volunteer_list, name='volunteer_list'),

        path('volunteer/approve/<int:id>/', approve_volunteer, name='approve_volunteer'),
        path('volunteer/delete/<int:id>/', delete_volunteer, name='delete_volunteer'),

        # gallery
         # gallery (donation list)
    # path('gallery/', gallery_list, name='gallery_list'),
    # path('gallery/delete/<int:id>/', delete_gallery, name='delete_gallery'),
    # path('gallery/', gallery_list, name='gallery_list'),
    # path('gallery/delete/<int:id>/', delete_gallery, name='delete_gallery'),
    # path("contact/", contact_list, name="contact"),


    ]

