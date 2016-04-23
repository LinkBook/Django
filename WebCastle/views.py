from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView

from . import forms


# Create your views here.

class Index(FormView):
    template_name = 'index.html'
    form_class = forms.RegisterForm
    success_url = '/admin'


class Categorys(View):
    def get(self, request, *args, **kwargs):
        return render(request, "all-Category.html")


class SiteMap(TemplateView):
    template_name = 'siteMap.html'


class Questions(TemplateView):
    template_name = 'Questions.html'


class ShowWebsites(TemplateView):
    template_name = 'showwebsites.html'

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


class Contact(TemplateView):
    template_name = 'contact.html'


class Vision(TemplateView):
    template_name = 'Vision.html'


class About(TemplateView):
    template_name = 'about.html'


class Websitepage1(TemplateView):
    template_name = 'websitepage1.html'


class Websitepage2(TemplateView):
    template_name = 'websitepage2.html'


class Websitepage3(TemplateView):
    template_name = 'websitepage3.html'
