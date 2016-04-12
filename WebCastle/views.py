from django.shortcuts import render
from django.views.generic import View
from django.views.generic.edit import FormView

from . import forms


# Create your views here.

class index(FormView):
    template_name = 'index.html'
    form_class = forms.RegisterForm
    success_url = '/about'

    def post(self, request, *args, **kwargs):
        return render(request, "about.html")


class categorys(View):
    def get(self, request, *args, **kwargs):
        return render(request, "all-Category.html")


class siteMap(View):
    def get(self, request, *args, **kwargs):
        return render(request, "siteMap.html")


class Questions(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Questions.html")


class showWebsites(View):
    def get(self, request, *args, **kwargs):
        return render(request, "showWebsites.html")


class contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contact.html")


class Vision(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Vision.html")


class about(View):
    def post(self, request):
        return render(request, "about.html")

    def get(self, request, *args, **kwargs):
        return render(request, "about.html")


class Websitepage1(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Websitepage1.html")


class Websitepage2(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Websitepage2.html")


class Websitepage3(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Websitepage3.html")
