from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import View
from django.views.generic.edit import FormView
from .forms import *
from .models import *

# Create your views here.
def Contact2(request):
    if request.method == "GET":
        return HttpResponse("ERROR")
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    form = Contact(name=name, email=email, message=message)
    contact = form.save()
    return render(request, 'contact.html')


class Index(FormView):
    template_name = 'index.html'
    form_class = RegisterForm
    success_url = '/admin'


def Comment2(request):
    if request.method == "GET":
        return HttpResponse("ERROR")
    comment_name = request.POST.get('name')
    comment_email = request.POST.get('email')
    comment = request.POST.get('comment')
    form = Comments(comment_name=comment_name, comment_email=comment_email, comment=comment)
    comments = form.save()
    return render(request, 'Websitepage1.html')


class Categorys(FormView):
    template_name = "all-Category.html"
    form_class = RegisterForm


def Register2(request):
    if request.method == "GET":
        return HttpResponse("ERROR")
    name = request.POST.get('name')
    username = request.POST.get('username')
    email = request.POST.get('user')
    password = request.POST.get('pass')
    rep = request.POST.get('rep')
    f = Karbar(name=name, username=username, email=email, password=password, rep=rep)
    karbar = f.save()
    return render(request, 'Websitepage1.html')


class SiteMap(FormView):
    template_name = 'siteMap.html'
    form_class = RegisterForm


def Login2(request):
    if request.method == "GET":
        return HttpResponse("ERROR")
    username = request.POST.get('username')
    password = request.POST.get('password')
    form = LoginForm({'username': username, 'password': password})
    login = form.save()
    return render(request, 'index.html')


class Questions(FormView):
    template_name = 'Questions.html'
    form_class = RegisterForm


# class index(FormView):
#     template_name = 'index.html'
#     form_class = RegisterForm
def index(request):
    webcontext = get_list_or_404(Webpage)
    print("zzz", webcontext)
    return render(request, 'index.html', {"webcontext": webcontext, "choice": 0})


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


class Categorys(View):
    def get(self, request, *args, **kwargs):
        return render(request, "all-Category.html")


class Contact(FormView):
    template_name = 'contact.html'
    form_class = RegisterForm


class SiteMap(View):
    def get(self, request, *args, **kwargs):
        return render(request, "siteMap.html")


class Vision(FormView):
    template_name = 'Vision.html'
    form_class = RegisterForm


class Questions(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Questions.html")


class About(FormView):
    template_name = 'about.html'
    form_class = RegisterForm


class ShowWebsites(View):
    def get(self, request, *args, **kwargs):
        return render(request, "showWebsites.html")


def Websitepage1(request, webtitle="1"):
    webcontext = get_object_or_404(Webpage, id=webtitle)
    return render(request, 'websitepage1.html', {"webcontext": webcontext})


def Websitepage2(request, webtitle="2"):
    webcontext = get_object_or_404(Webpage, id=webtitle)
    return render(request, 'websitepage2.html', {"webcontext": webcontext})


def Websitepage3(request, webtitle="3"):
    webcontext = get_object_or_404(Webpage, id=webtitle)
    return render(request, 'websitepage3.html', {"webcontext": webcontext})


class contact(View):
    def get(self, request, *args, **kwargs):
        return render(request, "contact.html")


class Vision(View):
    def get(self, request, *args, **kwargs):
        return render(request, "Vision.html")


class About(View):
    def post(self, request):
        return render(request, "about.html")

    def get(self, request, *args, **kwargs):
        return render(request, "about.html")
