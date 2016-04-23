# Register your models here.
from django.contrib import admin

import WebCastle.models as model

admin.site.register(model.Webpage)
admin.site.register(model.Category)
admin.site.register(model.SubCategory)
admin.site.register(model.Festival)
admin.site.register(model.Tag)
admin.site.register(model.Subscribe)
admin.site.site_header = ' لینک بوک '
