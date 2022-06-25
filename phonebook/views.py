from django.shortcuts import render
from .models import Contact

def index(request):
    contacts = Contact.objects.all()
    context = {
        "contacts": contacts
    }
    return render(request, 'phonebook/index.html', context)