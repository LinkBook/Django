# Register your models here.
from django.contrib import admin

import WebCastle.models as model


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email',)
    list_display = ('name', 'message', 'email')


class KarbarAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email')
    search_fields = ('username',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_name', 'comment_email', 'comment')
    search_fields = ('comment_name', 'comment_email',)


admin.site.register(model.Webpage)
admin.site.register(model.Category)
admin.site.register(model.SubCategory)
admin.site.register(model.Comments, CommentAdmin)
admin.site.register(model.Contact, ContactAdmin)
admin.site.register(model.Festival)
admin.site.register(model.Tag)
admin.site.register(model.Karbar, KarbarAdmin)
admin.site.register(model.Subscribe)
admin.site.site_header = ' لینک بوک '
