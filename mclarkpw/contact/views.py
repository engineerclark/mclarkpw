from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import ContactForm

class ContactMainView(FormView):
    template_name="contact/main.html"
    form_class = ContactForm