from django.urls import path

from .views import SMSFormView

urlpatterns = [
    path("", SMSFormView.as_view(), name="sms-form"),
]
