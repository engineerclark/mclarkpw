from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from .forms import ContactForm
from .models import Contact

class ContactMainView(FormView):
    template_name="contact/main.html"
    form_class = ContactForm
    
    def get_success_url(self):
        return reverse('contact.sent')
    
    def form_valid(self, form):
        if Contact.can_send():
            form.send_message()
        return super(ContactMainView, self).form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super(ContactMainView, self).get_context_data(**kwargs)
        
        # Values to be loaded dynamically
        context['can_send'] = Contact.can_send()
        
        return context

class ContactSentView(TemplateView):
    template_name="contact/sent.html"