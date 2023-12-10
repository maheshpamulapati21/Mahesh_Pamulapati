from django.shortcuts import render, get_object_or_404, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.
# My_Contacts/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World!")


# polls/urls.py

# my_site/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("MY_Contacts/", include("MY_Contacts.urls")),
    path("admin/", admin.site.urls),
]



# View to list all contacts
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

# View to create a new contact
def contact_new(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', id=contact.id)
    else:
        form = ContactForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

# View to display contact details
def contact_detail(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})

# View to edit an existing contact
def contact_edit(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', id=contact.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/contact_form.html', {'form': form})

# View to delete a contact
def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == "POST":
        contact.delete()
        return redirect('contact_list')
    return render(request, 'contacts/contact_confirm_delete.html', {'contact': contact})

