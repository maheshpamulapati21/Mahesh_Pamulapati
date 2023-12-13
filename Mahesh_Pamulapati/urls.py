from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('MY_Contacts.urls', namespace='MY_Contacts')),  # Include and set the app's namespace
    path('admin/', admin.site.urls),
]
