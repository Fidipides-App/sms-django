import requests
from celery import shared_task

from .utils import format_phone_number


@shared_task
def send_sms(phone: str, message: str) -> str:
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
