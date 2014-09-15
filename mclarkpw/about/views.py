from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import *
import datetime

class MainView(View):
    template_name="about/main.html"
    
    @classmethod
    def sort_date(cls, item):
        key = item.end_date
        if not key:
            key = datetime.date.today() + datetime.timedelta(days=365)
        return key
        
    def get(self, request, *args, **kwargs):
        positions = sorted(list(Position.objects.all()), key=MainView.sort_date, reverse=True)
        schools = sorted(list(School.objects.all()), key=MainView.sort_date, reverse=True)
        data = {'positions':positions, 'schools':schools}
        return render(request, self.template_name, data)
        