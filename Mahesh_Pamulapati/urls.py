"""
URL configuration for Mahesh_Pamulapati project.

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

from django.urls import include, path
from django.contrib import admin
from MY_Contacts import views as contact_views

urlpatterns = [
    path('', contact_views.contact_list, name='home'),  # Set the contact list as the homepage
    path('MY_Contacts/', include('MY_Contacts.urls')),
    path('admin/', admin.site.urls),
]





