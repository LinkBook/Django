"""LinkBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from WebCastle.views import *

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^web/', include('WebCastle.urls', namespace='Webcastel')),
                  url(r'^$', Index.as_view(), name='Home'),
                  url(r'^index$', Index.as_view()),
                  url(r'^all-Category$', Categorys.as_view(), name='all-Category'),
                  url(r'^siteMap$', SiteMap.as_view(), name='siteMap'),
                  url(r'^Questions$', Questions.as_view(), name='Questions'),
                  url(r'^showWebsites$', ShowWebsites.as_view(), name='showWebsites'),
                  url(r'^contact$', Contact.as_view(), name='contact'),
                  url(r'^Vision$', Vision.as_view(), name='Vision'),
                  url(r'^about$', About.as_view(), name='about'),
                  url(r'^Websitepage1$', Websitepage1, name='Websitepage1'),
                  url(r'^Websitepage2$', Websitepage2, name='Websitepage2'),
                  url(r'^Websitepage3$', Websitepage3, name='Websitepage3'),
              ] + static(settings.MEDIA_URL, MEDIA_ROOT=settings.MEDIA_ROOT)
