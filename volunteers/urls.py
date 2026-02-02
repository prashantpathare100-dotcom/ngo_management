from django.urls import path
from .views import volunteer_list

app_name = 'volunteers'

urlpatterns = [
    path('', volunteer_list, name='volunteer_list'),
]
