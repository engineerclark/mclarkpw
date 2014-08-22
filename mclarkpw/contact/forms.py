from django import forms
from .models import Contact

class ContactForm(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'name'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder':'email'}))
    subject = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'subject/reason for contact'}))
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'message'}))
    
    def send_message(self):
        contact_message = Contact()
        contact_message.name = self.cleaned_data['name']
        contact_message.email = self.cleaned_data['email']
        contact_message.subject = self.cleaned_data['subject']
        contact_message.message = self.cleaned_data['message']
        contact_message.save()
        contact_message.send()
        
    