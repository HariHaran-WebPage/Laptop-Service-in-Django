"""
URL configuration for Service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Web import views
from Web.views import check_email_existence
from Web.views import change_password


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('About', views.About, name='About'),
    path('Service', views.Service, name='Service'),
    path('Contact', views.Contact, name='Contact'),
    path('login/', views.Login, name='Login'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
    path('signup/', views.sign_up, name='signup'),
    path('check_email/', check_email_existence, name='check_email'), 
     path('change_password/', change_password, name='change_password'),
     

  
]

