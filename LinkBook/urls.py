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
import django.contrib.auth.urls
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views.generic import RedirectView
from material.frontend import urls as frontend_urls
from WebCastle.views import *

# from django.conf.urls import ( handler400, handler403, handler404, handler500)

# handler400 = 'WebCastle.views.bad_request'
# handler403 = 'WebCastle.views.permission_denied'
# handler404 = 'WebCastle.views.page_not_found'
# handler500 = 'WebCastle.views.server_error'

urlpatterns = [
                  url('^', include('django.contrib.auth.urls')),
                  # url(r'', include(frontend_urls)),
                  # url('^change-password/', auth_views.password_change),
                  # url(r'^web/', include('WebCastle.urls')),
                  # url(r'^accounts/', include('allauth.urls')),
                  url(r'^admin/', admin.site.urls),
                  url(r'^web/', include('WebCastle.urls', namespace='Webcastel')),
                  url(r'^$', Index.as_view(), name='Home'),
                  url(r'^$', RedirectView.as_view(url='/web', permanent=True)),
                  url(r'^index$', Index.as_view(), name='index'),
                  url(r'^all-Category$', Categorys.as_view(), name='all-Category'),
                  url(r'^siteMap$', SiteMap.as_view(), name='siteMap'),
                  url(r'^Questions$', Questions.as_view(), name='Questions'),
                  url(r'^showWebsites-(?P<web>[\w-]+)', ShowWebsites, name='showWebsites'),
                  url(r'^showWebsites', ShowWebsites, name='showWebsites'),
                  url(r'^contact$', Contact.as_view(), name='contact'),
                  url(r'^Vision$', Vision.as_view(), name='Vision'),
                  url(r'^about$', About.as_view(), name='about'),
                  url(r'^Websitepage-(?P<webtitle>[\w-]+)', Websitepage, name='Websitepage'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
