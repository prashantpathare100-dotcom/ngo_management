from django.urls import path
from .views import volunteers_page

urlpatterns = [
    path('volunteers/', volunteers_page, name='website_volunteers'),
]
