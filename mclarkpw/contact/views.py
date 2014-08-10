from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from .forms import ContactForm

class ContactMainView(FormView):
    template_name="contact/main.html"
    form_class = ContactForm
    
    def get_success_url(self):
        return reverse('contact.sent')
    
    def form_valid(self, form):
        form.send_message()
        return super(ContactMainView, self).form_valid(form)
    

class ContactSentView(TemplateView):
    template_name="contact/sent.html"