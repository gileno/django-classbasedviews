#encoding: utf-8

from django.views.generic import View, TemplateView
from django.shortcuts import render


class Home1(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'home1.html')


class Home2(TemplateView):

    template_name = 'home2.html'


class Home4(TemplateView):

    template_name = 'home4.html'

    def get_context_data(self, **kwargs):
        context = super(Home4, self).get_context_data(**kwargs)
        context['name'] = u'Gileno Filho'
        return context