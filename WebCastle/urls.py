from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from .views import *

urlpatterns = [
                  url(r'^$', Index.as_view(), name='Home'),
                  # url(r'^$', RedirectView.as_view(url='/myapp/list/', permanent=True)),
                  url(r'^admin/', admin.site.urls),
                  # url(r'^ind$', index.as_view()),
                  url(r'^index$', index),
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
                  url(r'^contact.html$', Contact2),
                  url(r'^login$', Login2),
                  url(r'^index$', Register2),
                  url(r'^webpage$', Comment2),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
