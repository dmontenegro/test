# Create your views here.
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView, FormView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.urlresolvers import reverse_lazy
#from .models import Inventory, Perfiles
from .forms import UserForm

import forms

class Registrarse(FormView):
	template_name = 'registrarse.html'
	form_class = UserForm
	success_url = reverse_lazy('registrarse')

	def form_valid(self, form):
		user = form.save()
		user.save()
		return HttpResponseRedirect(reverse_lazy('books_cbv'))


