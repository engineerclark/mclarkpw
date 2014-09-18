from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class WebDevMainView(TemplateView):
    template_name="webdev/main.html"
    
    def get(self, request, *args, **kwargs):
        projects = Project.objects.all()
        data = {'projects':projects}
        return render(request, self.template_name, data)
