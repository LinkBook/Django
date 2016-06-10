from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import FormView

from .forms import *
from .models import *

TeLib = template.Library()


# Create your views here.

class Index(FormView):
    template_name = 'index.html'
    form_class = RegisterForm
    success_url = '/admin'


class Categorys(FormView):
    template_name = "all-Category.html"
    form_class = RegisterForm


class SiteMap(FormView):
    template_name = 'siteMap.html'
    form_class = RegisterForm


class Questions(FormView):
    template_name = 'Questions.html'
    form_class = RegisterForm


class ShowWebsites(FormView):
    template_name = 'showwebsites.html'
    form_class = RegisterForm

    def get_context_data(self, **kwargs):
        context = super(ShowWebsites, self).get_context_data(**kwargs)
        webs = []
        for i in range(100):
            webs.append('%s' % (i + 1))
        paginator = Paginator(webs, 24)
        page = self.request.GET.get('page')
        try:
            show_webs = paginator.page(page)
        except PageNotAnInteger:
            show_webs = paginator.page(1)
        except EmptyPage:
            show_webs = paginator.page(paginator.num_pages)
        context['webs'] = show_webs
        return context


class Contact(FormView):
    template_name = 'contact.html'
    form_class = RegisterForm


class Vision(FormView):
    template_name = 'Vision.html'
    form_class = RegisterForm


class About(FormView):
    template_name = 'about.html'
    form_class = RegisterForm


def Websitepage1(request, webtitle="چگونه دات آی آر"):
    webcontext = get_object_or_404(Webpage, title=webtitle)
    return render(request, 'websitepage1.html', {"webcontext": webcontext})


def Websitepage2(request, webtitle="تیم لاک "):
    webcontext = get_object_or_404(Webpage, title=webtitle)
    return render(request, 'websitepage2.html', {"webcontext": webcontext})


def Websitepage3(request, webtitle="تیم لاک "):
    webcontext = get_object_or_404(Webpage, title=webtitle)
    return render(request, 'websitepage3.html', {"webcontext": webcontext})
