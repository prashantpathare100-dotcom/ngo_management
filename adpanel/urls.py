from django.urls import path

from adpanel import views

urlpatterns = [

]

from . import views

from .views import (
        volunteer_list,
        approve_volunteer,
        delete_volunteer,
        contact_list   
        
    )
    

urlpatterns = [
    # volunteers
     path("dashboard/volunteers/", views.volunteer_list, name="volunteer_list"),
    path('volunteer/approve/<int:id>/', approve_volunteer, name='approve_volunteer'),
    path('volunteer/delete/<int:id>/', delete_volunteer, name='delete_volunteer'),
    path("contact/", contact_list, name="contact"),

    path("dashboard/contact/", contact_list, name="contact_list"),
    path("basic_info/", views.basic_info, name="basic_info"),
    path("save_basic_info/", views.save_basic_info, name="save_basic_info"),
    path("basic_info/delete/<int:id>/", views.delete_basic_info, name="delete_basic_info"),

    # testiomoinsal
    path("testionmals_info/", views.testionmals_info, name="testionmals_info"),

    
]