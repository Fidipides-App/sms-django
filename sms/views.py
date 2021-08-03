from django.views.generic.edit import FormView

from .forms import SMSForm


class SMSFormView(FormView):
    form_class = SMSForm
    template_name = "sms/form.html"
    success_url = "/sms"
