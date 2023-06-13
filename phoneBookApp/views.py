from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm, NumberForm


def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})


def add_contact(request):
    NumberFormSet = formset_factory(NumberForm, extra=1)
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        number_formset = NumberFormSet(request.POST, prefix='numbers')
        #if contact_form.is_valid() and number_formset.is_valid():            
        contact = contact_form.save()
        
        for number_form in number_formset:
            number = number_form.save(commit=False)
            number.contact = contact
            number.save()
        return redirect('contact-list')

    else:
        contact_form = ContactForm()
        number_formset = NumberFormSet(prefix='numbers')
    return render(request, 'add_contact.html', {'contact_form': contact_form, 'number_formset': number_formset})

def contact_detail(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    return render(request, 'contact_detail.html', {'contact': contact})