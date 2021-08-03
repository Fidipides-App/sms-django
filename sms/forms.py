from django import forms


class SMSForm(forms.Form):
    phone_number = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
