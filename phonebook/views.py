from django.shortcuts import render, redirect
from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, 'phonebook/index.html', context)


def contact_detail(request, id):
    contact = Contact.objects.get(id=id)
    context = {
        "contact": contact
    }
    return render(request, 'phonebook/contact_detail.html', context)


def contact_delete(request, id):
    contact = Contact.objects.get(id=id)
    contact.delete()
    return redirect("/")