from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactoForm
from django.contrib import messages
from django.views.generic import CreateView
from django.urls import reverse_lazy
from typing import Any

# Create your views here.

class ContactoUsuario(CreateView):
    template_name='contacto/contacto.html'
    form_class=ContactoForm
    success_url=reverse_lazy('home')

    def get_context_data(self, **kwargs: reverse_lazy) -> dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['request']=self.request
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        messages.success(self.request, 'Consulta enviada')
        return super().form_valid(form)