from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'name'}))
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'placeholder':'email'}))
    subject = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'subject/reason for contact'}))
    message = forms.CharField(label='',widget=forms.Textarea(attrs={'placeholder':'message'}))
    