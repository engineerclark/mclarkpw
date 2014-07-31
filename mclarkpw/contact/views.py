from django.shortcuts import render
from django.views.generic import TemplateView

class ContactMainView(TemplateView):
    template_name="contact/main.html"