from django.shortcuts import render, redirect
from django.views import View

class Index(View):
    model = 'Elogio'
    template_name = 'Elogio/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
