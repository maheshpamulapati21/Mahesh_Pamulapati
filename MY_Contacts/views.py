from django.shortcuts import render, redirect
from .models import Contact  # Import your Contact model
from .forms import ContactForm  # Import your contact form

def contact_list(request):
    contacts = Contact.objects.all()  # Retrieve all contacts from the database
    context = {'contact': contacts}
    return render(request, 'MY_Contacts/contact_list.html', context)

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the contact data to the database
            form.save()
            return redirect('MY_Contacts:contact_list.html')
    else:
        form = ContactForm()
    
    context = {'form': form}
    return render(request, 'MY_Contacts/contact_create.html', context)

from django.shortcuts import render, get_object_or_404

def contact_detail(request, id):
    contact = get_object_or_404(Contact, id=id)  # Retrieve the contact by its ID
    context = {'contact': contacts}
    return render(request, 'MY_Contacts/contact_detail.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact  # Import your Contact model
from .forms import ContactForm  # Import your contact form

def contact_edit(request, id):
    contact = get_object_or_404(Contact, id=id)  # Retrieve the contact by its ID

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('MY_Contacts:contact_detail', id=id)  # Redirect to the contact detail page
    else:
        form = ContactForm(instance=contact)
    
    context = {'form': form, 'contact': contacts}
    return render(request, 'MY_Contacts/contact_update.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact  # Import your Contact model

def contact_delete(request, id):
    contact = get_object_or_404(Contact, id=id)  # Retrieve the contact by its ID

    if request.method == 'POST':
        contact.delete()
        return redirect('MY_Contacts:contact_list')  # Redirect to the contact list
    
    context = {'contact': contacts}
    return render(request, 'MY_Contacts/contact_confirm_delete.html', context)