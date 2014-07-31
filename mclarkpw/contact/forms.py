from django import forms

class ContactForm(forms.form):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'placeholder':'name'}))
    email = forms.EmailField(label='email', widget=forms.TextInput(attrs={'placeholder':'email'}))
    subject = forms.CharField(label='subject/reason for contact', widget=forms.TextInput(attrs={'placeholder':'subject/reason for contact'}))
    message = forms.CharField(label='subject/reason for contact', widget=forms.Textarea(attrs={'placeholder':'subject/reason for contact'}))
    