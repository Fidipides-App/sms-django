from django.contrib import messages
from django.views.generic.edit import FormView

from .forms import SMSForm
from .tasks import send_sms
from .utils import format_phone_number


class SMSFormView(FormView):
    form_class = SMSForm
    template_name = "sms/form.html"
    success_url = "/sms"

    def form_valid(self, form):
        phone_number = form.cleaned_data["phone_number"]
        message = form.cleaned_data["message"]

        send_sms.delay(phone_number, message)
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Mensagem para {0} colocada em fila para envio.".format(format_phone_number(phone_number)),
        )

        return super().form_valid(form)
