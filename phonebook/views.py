from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

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

def contact_create(request):
    if request.method == "POST":
        first_name = request.POST['first_name'] if request.POST['first_name'] else None
        last_name = request.POST['last_name'] if request.POST['last_name'] else None
        phone_number = request.POST['phone_number'] if request.POST['phone_number'] else None
        if None not in [first_name, last_name, phone_number]:
            Contact.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number)
        else:
            messages.error(request, "All Fields Should Be Filled")
            return redirect("/create")
        return redirect("/")
    elif request.method == "GET":
        return render(request, "phonebook/contact_create.html")
