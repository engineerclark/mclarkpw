from django.shortcuts import render
from django.views.generic import TemplateView

class EnterpriseMainView(TemplateView):
    template_name="enterprise/main.html"
