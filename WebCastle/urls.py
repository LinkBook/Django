from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from .views import *

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^all-Category$', Categorys.as_view(), name='all-Category'),
                  url(r'^siteMap$', SiteMap.as_view(), name='siteMap'),
                  url(r'^Questions$', Questions.as_view(), name='Questions'),
                  url(r'^contact$', Contact.as_view(), name='contact'),
                  url(r'^Vision$', Vision.as_view(), name='Vision'),
                  url(r'^about$', About.as_view(), name='about'),
                  url(r'^Websitepage-(?P<webtitle>[\w-]+)', Websitepage, name='Websitepage'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
