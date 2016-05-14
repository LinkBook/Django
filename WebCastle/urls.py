from django.conf.urls import url
from django.contrib import admin

from .views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name='Home'),
    url(r'^index$', Index.as_view()),
    url(r'^all-Category$', Categorys.as_view(), name='all-Category'),
    url(r'^siteMap$', SiteMap.as_view(), name='siteMap'),
    url(r'^Questions$', Questions.as_view(), name='Questions'),
    url(r'^showWebsites$', ShowWebsites.as_view(), name='showWebsites'),
    url(r'^contact$', Contact.as_view(), name='contact'),
    url(r'^Vision$', Vision.as_view(), name='Vision'),
    url(r'^about$', About.as_view(), name='about'),
    # url(r'^Websitepage1$', Websitepage1.as_view(), name='Websitepage1'),
    url(r'^Websitepage1$', Webpage, name='Websitepage1'),
    url(r'^Websitepage2$', Websitepage2.as_view(), name='Websitepage2'),
    url(r'^Websitepage3$', Websitepage3.as_view(), name='Websitepage3'),
]
