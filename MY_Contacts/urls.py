from django.urls import path
from . import views


urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('contact/', views.contact_new, name='contact_form'),
    path('contact/<int:id>/', views.contact_detail, name='contact_detail'),
    path('contact/<int:id>/edit/', views.contact_edit, name='contact_update'),
    path('contact/<int:id>/delete/', views.contact_delete, name='contact__confirm_delete'),
]
