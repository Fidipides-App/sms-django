from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView

from .models import Patient


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "search/home.html"


class SearchView(LoginRequiredMixin, TemplateView):
    template_name = "search/search.html"


"""
class SearchResultView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "search/result.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Patient.objects.get(phone=query)
        return object_list
"""


class SearchResultView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = "search/result.html"
    context_object_name = "patient"

    def get_queryset(self):
        result = super(SearchResultView, self).get_queryset()
        query = self.request.GET.get("q")
        if query:
            patient_data = Patient.objects.filter(phone=query)
            result = patient_data
        else:
            messages.add_message(self.request, messages.ERROR, "No patient with tha phone number found!")
            result = None
        return result
