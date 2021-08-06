from datetime import date
from time import sleep

import requests
from celery import shared_task

from search.models import Patient

from .config import BIRTHDAY_MESSAGE
from .utils import format_phone_number


@shared_task
def send_sms(phone: str, message: str):
    """Send an SMS message"""
    api_url = "http://172.16.0.67:8080"
    api_endpoint = "/v1/sms/"

    data = {
        "phone": format_phone_number(phone),
        "message": message,
    }

    res = requests.post(api_url + api_endpoint, data=data)

    if res.content.decode("utf-8") == "OK":
        print("Mensagem para {0} enviada!".format(data.get("phone")))
        return "Mensagem para {0} colocada em fila de espera para envio.".format(data.get("phone"))
    else:
        print("Erro ao enviar a mensagem.")
        return None


@shared_task
def send_birthday_sms():
    today = date.today()
    users = Patient.objects.filter(birthdate__month=today.month, birthdate__day=today.day)
    # cron_result = []

    for user in users:
        print("Sending SMS to {0} ({1})".format(user.name, user.phone))
        res = send_sms.delay(user.phone, BIRTHDAY_MESSAGE.format(user.name))
        print(res)
        sleep(5)
        # cron_result += res

    # return cron_result
    return None
