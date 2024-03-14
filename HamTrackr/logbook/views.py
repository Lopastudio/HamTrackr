from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm, SignUpForm
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth import logout
from django.urls import reverse


def home_page(request):
    template = loader.get_template("home.html")
    return HttpResponse(template.render({}, request))

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'logbook/contact_list.html', {'contacts': contacts})

def edit_contact(request, contact_id):
    # Retrieve the contact object using the provided contact_id
    contact = get_object_or_404(Contact, id=contact_id)
    
    # Check if the request method is POST, indicating form submission for editing
    if request.method == 'POST':
        # Assuming you have a ContactForm defined for editing contacts
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            # Redirect to the contact list page or any other appropriate page
            return redirect('contact_list')
    else:
        # Create a form instance pre-filled with the contact's data
        form = ContactForm(instance=contact)
    
    # Render the edit contact form template with the form and contact object
    return render(request, 'logbook/edit_contact.html', {'form': form, 'contact': contact})

def log_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'logbook/log_contact.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})