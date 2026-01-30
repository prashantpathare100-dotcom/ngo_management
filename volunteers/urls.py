from django.urls import path
from .views import website_volunteer_submit

urlpatterns = [
    path(
        'submit/',
        website_volunteer_submit,
        name='website_volunteer_submit'
    ),
]
