from django.conf.urls import url
from django.conf.urls.static import static
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
                  url(r'^Websitepage1$', Websitepage1, name='Websitepage1'),
                  url(r'^Websitepage2$', Websitepage2, name='Websitepage2'),
                  url(r'^Websitepage3$', Websitepage3, name='Websitepage3'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
