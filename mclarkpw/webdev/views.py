from django.shortcuts import render
from django.views.generic import TemplateView

class WebDevMainView(TemplateView):
    template_name="webdev/main.html"
