from django.urls import path
from . import views

urlpatterns = [
    # Donation routes (as it is)
    path("gallery_page/", views.gallery_page, name="gallery_page"),
    path("gallery_list/", views.gallery_list, name="gallery_list"),
    path("delete_gallery/<int:id>/", views.delete_gallery, name="delete_gallery"),

]


