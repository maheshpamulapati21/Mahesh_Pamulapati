from django.urls import path
from . import views

app_name = 'MY_Contacts'  

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('create/', views.contact_create, name='contact_create'),
    path('<int:id>/', views.contact_detail, name='contact_detail'),
    path('<int:id>/edit/', views.contact_edit, name='contact_update'),
    path('<int:id>/delete/', views.contact_delete, name='contact_confirm_delete'),
]
