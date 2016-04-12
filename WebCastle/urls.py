from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^$', index.as_view(), name='Home'),
    url(r'^index$', index.as_view()),
    url(r'^all-Category$', categorys.as_view(), name='all-Category'),
    url(r'^siteMap$', siteMap.as_view(), name='siteMap'),
    url(r'^Questions$', Questions.as_view(), name='Questions'),
    url(r'^showWebsites$', showWebsites.as_view(), name='showWebsites'),
    url(r'^contact$', contact.as_view(), name='contact'),
    url(r'^Vision$', Vision.as_view(), name='Vision'),
    url(r'^about$', about.as_view(), name='about'),
    url(r'^Websitepage1$', Websitepage1.as_view(), name='Websitepage1'),
    url(r'^Websitepage2$', Websitepage2.as_view(), name='Websitepage2'),
    url(r'^Websitepage3$', Websitepage3.as_view(), name='Websitepage3'),
]
