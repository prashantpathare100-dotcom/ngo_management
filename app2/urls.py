"""
URL configuration for app2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adpanel import views as adpanel
from website import views as users
from django.contrib.auth.views import LogoutView  
from adpanel.views import dashboard_view , login_view  
from website import views as ui
from django.urls import reverse_lazy


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',ui.home),
    path('terms/',ui.terms),
    path('privacy/',ui.privacy),
    path('faq/',ui.faq),
    path('contact/',ui.contact),
    path('donate/',ui.donate),
    path('about/',ui.about),
    path('events/',ui.events),
    path('volunteers/',ui.volunteers),
    path('gallery/',ui.gallery),
    path('causes_programs/',ui.causes_programs),
    path('testimonials/',ui.testimonials),
    path('blog_news/',ui.blog_news),
    path("admin/", login_view, name="login"),

    path("login/", dashboard_view, name="dashboard"),

    path(
        "logout/",
        LogoutView.as_view(next_page=reverse_lazy("login")),
        name="logout"
    )
]


