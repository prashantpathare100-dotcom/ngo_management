from django.urls import path

from .views import volunteer_list

app_name = 'volunteers'

urlpatterns = [
    path('', volunteer_list, name='volunteer_list'),
]
from .views import website_volunteer_submit

urlpatterns = [
    path(
        'submit/',
        website_volunteer_submit,
        name='website_volunteer_submit'
    ),

]
