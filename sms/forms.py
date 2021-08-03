from django import forms


class SMSForm(forms.Form):
    phone_number = forms.TextInput()
    message = forms.Textarea()
