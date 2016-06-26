from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, render_to_response
from django.views.generic import View
from django.views.generic.edit import FormView
from .forms import *
from .models import *


# HTTP Error 404
# def page_not_found(request):
#     response = render_to_response(
#         '404.html',
#         context_instance=RequestContext(request)
#     )
#
#     response.status_code = 404
#
#     return response

class About(FormView):
    template_name = 'about.html'
    form_class = ReistrationForm
    success_url = "/index"

    def get_context_data(self, **kwargs):
        context = super(About, self).get_context_data(**kwargs)
        KasbTags = SubCategory.objects.filter(category__category_name="کسب وکارهای آنلاین")
        EtelaTags = SubCategory.objects.filter(category__category_name="اطلاع رسانی و محتوا")
        ShaTags = SubCategory.objects.filter(category__category_name="شخصی و شرکتی")
        KhaTags = SubCategory.objects.filter(category__category_name="خدمات آنلاین")
        Username = self.request.user
        context['ETags'] = EtelaTags
        context['KTags'] = KasbTags
        context['STags'] = ShaTags
        context['KhTags'] = KhaTags
        context['username'] = Username
        return context

    def form_valid(self, form):
        form.save()
        return super(About, self).form_valid(form)


class Index(About):
    template_name = 'index.html'
    webcontext = Webpage.objects.all()

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        webcontext = Webpage.objects.all()
        context['webcontext'] = webcontext
        return context


class Categorys(About):
    template_name = "all-Category.html"


class SiteMap(About):
    template_name = "siteMap.html"


class Questions(About):
    template_name = "Questions.html"


class Contact(About):
    template_name = "contact.html"


class Vision(About):
    template_name = "Vision.html"


def Contact2(request):
    if request.method == "GET":
        return HttpResponse("ERROR")
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    form = Contact(name=name, email=email, message=message)
    contact = form.save()
    return render(request, 'contact.html')





def ShowWebsites(request, web="1"):
    form = ReistrationForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
    webcontext = Webpage.objects.filter(Sub__id=web)
    Sub = SubCategory.objects.filter(id=web)
    KasbTags = SubCategory.objects.filter(category__category_name="کسب وکارهای آنلاین")
    EtelaTags = SubCategory.objects.filter(category__category_name="اطلاع رسانی و محتوا")
    ShaTags = SubCategory.objects.filter(category__category_name="شخصی و شرکتی")
    KhaTags = SubCategory.objects.filter(category__category_name="خدمات آنلاین")
    Username = request.user

    context = {"webcontext": webcontext, 'form': form, "ETags": EtelaTags, 'KTags': KasbTags, 'STags': ShaTags,
               'KhTags': KhaTags, "username": Username, "sub": Sub}
    return render(request, 'showWebsites.html', context)


def Websitepage(request, webtitle="1"):
    form = ReistrationForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
    Username = request.user
    webcontext = get_object_or_404(Webpage, id=webtitle)
    Fescontext = Festival.objects.filter(webpage=webcontext.id)
    KasbTags = SubCategory.objects.filter(category__category_name="کسب وکارهای آنلاین")
    EtelaTags = SubCategory.objects.filter(category__category_name="اطلاع رسانی و محتوا")
    ShaTags = SubCategory.objects.filter(category__category_name="شخصی و شرکتی")
    KhaTags = SubCategory.objects.filter(category__category_name="خدمات آنلاین")
    Tags = webcontext.Sub.all()
    context = {"webcontext": webcontext, "Fescontext": Fescontext, "Tags": Tags, 'form': form, "username": Username,
               "ETags": EtelaTags, 'KTags': KasbTags, 'STags': ShaTags,
               'KhTags': KhaTags}
    return render(request, 'Websitepage.html', context)
