from django.urls import path
from .views import contact, contact_list

urlpatterns = [
    path('', contact, name='contact'),   # ✅ website page
    path('dashboard/messages/', contact_list, name='contact_list'),  # ✅ dashboard
]
