from django.urls import path
from adpanel import views

urlpatterns = [
    path("donations/", views.admin_donations, name="admin_donations"),
    path("donations/", views.admin_donations, name="admin_donations"),
    # path('donations/', views.donations_list, name='donations_list'),
    # path('donations/add/', views.donar_data, name='donar_data'),
    # path('donations/edit/<int:id>/', views.donation_edit, name='donation_edit'),
    # path('donations/delete/<int:id>/', views.donation_delete, name='donation_delete'),
    # path('donations/add/', views.donar_data, name='donation_add'),
]

