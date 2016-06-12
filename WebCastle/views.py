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


# Create your views here.

# def index(request, ):
#     webcontext = get_list_or_404(Webpage)
#     form = ReistrationForm(request.POST or None)
#     if form.is_valid():
#         new_user = form.save(commit=False)
#         new_user.is_staff = True
#         new_user.save()
#     # return redirect('/admin')
#     context = {"form": form, "webcontext": webcontext}
#     return render(request, "index.html", context)


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
        print("Tag::", KasbTags)
        context['ETags'] = EtelaTags
        context['KTags'] = KasbTags
        context['STags'] = ShaTags
        context['KhTags'] = KhaTags
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super(About, self).form_valid(form)


class Index(About):
    template_name = 'index.html'
    webcontext = get_list_or_404(Webpage)

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['webcontext'] = Index.webcontext
        return context


# class ShowWebsites(About):
#     template_name = 'showwebsites.html'
#     count = Webpage.objects.filter().count()
#     print(count)
#     SubCat = 1
#     print("SubCAt::", SubCat)
#
#     def get_context_data(self, **kwargs):
#         context = super(ShowWebsites, self).get_context_data(**kwargs)
#         # webs = get_list_or_404(Webpage)
#         webs = Webpage.objects.filter(Sub__id=ShowWebsites.SubCat)
#         print("webs=", webs)
#         for i in range(ShowWebsites.count):
#             webs
#         paginator = Paginator(webs, 24)
#         page = self.request.GET.get('page')
#         try:
#             show_webs = paginator.page(page)
#         except PageNotAnInteger:
#             show_webs = paginator.page(1)
#         except EmptyPage:
#             show_webs = paginator.page(paginator.num_pages)
#         context['webs'] = show_webs
#         return context


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


def Comment2(request):
    if request.method == "GET":
        return HttpResponse("ERROR")
    comment_name = request.POST.get('name')
    comment_email = request.POST.get('email')
    comment = request.POST.get('comment')
    form = Comments(comment_name=comment_name, comment_email=comment_email, comment=comment)
    comments = form.save()
    return render(request, 'Websitepage.html')


def ShowWebsites(request, web="1"):
    form = ReistrationForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)
    webcontext = get_list_or_404(Webpage, Sub__id=web)
    # Fescontext = Festival.objects.filter(webpage=webcontext.id)
    # Tags = SubCategory.objects.all()
    print("zzz", webcontext, "zzzz")
    KasbTags = SubCategory.objects.filter(category__category_name="کسب وکارهای آنلاین")
    EtelaTags = SubCategory.objects.filter(category__category_name="اطلاع رسانی و محتوا")
    ShaTags = SubCategory.objects.filter(category__category_name="شخصی و شرکتی")
    KhaTags = SubCategory.objects.filter(category__category_name="خدمات آنلاین")
    context = {"webcontext": webcontext, 'form': form, "ETags": EtelaTags, 'KTags': KasbTags, 'STags': ShaTags,
               'KhTags': KhaTags}
    return render(request, 'showwebsites.html', context)


def Websitepage(request, webtitle="1"):
    form = ReistrationForm(request.POST or None)
    if form.is_valid():
        form.save(commit=False)

    webcontext = get_object_or_404(Webpage, id=webtitle)
    Fescontext = Festival.objects.filter(webpage=webcontext.id)
    Tags = webcontext.Sub.all()
    context = {"webcontext": webcontext, "Fescontext": Fescontext, "Tags": Tags, 'form': form}
    return render(request, 'Websitepage.html', context)
