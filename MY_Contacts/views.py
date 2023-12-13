from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm

def contact_list(request):
    contacts = Contact.objects.all()
    context = {'contacts': contacts}
    return render(request, 'MY_Contacts/contact_list.html', context)

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('MY_Contacts:contact_list')  # Redirect to the contact list page
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'MY_Contacts/contact_create.html', context)

def contact_detail(request, id):
    contact = get_object_or_404(Contact, id=id)
    context = {'contact': contact}
    return render(request, 'MY_Contacts/contact_detail.html', context)

def contact_edit(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('MY_Contacts:contact_detail', id=id)  # Redirect to the contact detail page
    else:
        form = ContactForm(instance=contact)
    
    context = {'form': form, 'contact': contact}
    return render(request, 'MY_Contacts/contact_update.html', context)

def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('MY_Contacts:contact_list')  # Redirect to the contact list page
    else:
        context = {'contact': contact}
        return render(request, 'MY_Contacts/contact_confirm_delete.html', context)

def contact_update(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)

    if request.method == 'POST':
        # Handle form submission and update the contact
        contact.first_name = request.POST['first_name']
        contact.last_name = request.POST['last_name']
        contact.phone_number = request.POST['phone_number']
        contact.save()
        return redirect('MY_Contacts:contact_list')  # Redirect to the contact list page after editing

    return render(request, 'MY_Contacts/contact_update.html', {'contact': contact})
