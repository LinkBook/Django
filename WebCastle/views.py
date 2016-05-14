from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .models import *


# Create your views here.

class Index(FormView):
    template_name = 'index.html'
    form_class = forms.RegisterForm
    success_url = '/admin'


class Categorys(FormView):
    template_name = "all-Category.html"
    form_class = forms.RegisterForm


class SiteMap(FormView):
    template_name = 'siteMap.html'
    form_class = forms.RegisterForm


class Questions(FormView):
    template_name = 'Questions.html'
    form_class = forms.RegisterForm


class ShowWebsites(FormView):
    template_name = 'showwebsites.html'
    form_class = forms.RegisterForm

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
    form_class = forms.RegisterForm


class Vision(FormView):
    template_name = 'Vision.html'
    form_class = forms.RegisterForm


class About(FormView):
    template_name = 'about.html'
    form_class = forms.RegisterForm


# class Websitepage1(TemplateView):
#     template_name = 'websitepage1.html'
def Webpage(request):
    tempname = 'websitepage1.html'
    f = Festival.objects.filter(fest_title="چگونه")
    print(str(f))
    print(type(f))
    return render(request, tempname, {"F": f})


class Websitepage2(TemplateView):
    template_name = 'websitepage2.html'


class Websitepage3(TemplateView):
    template_name = 'websitepage3.html'
