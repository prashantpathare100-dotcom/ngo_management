from django.urls import path
from .views import volunteer_list

urlpatterns = [
    path('volunteers/', volunteer_list, name='volunteer_list'),
]
