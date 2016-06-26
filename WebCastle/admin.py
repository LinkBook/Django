# Register your models here.
from django.contrib import admin
import WebCastle.models as model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

from WebCastle import models


class WebpageAdmin(admin.ModelAdmin):
    fields = ('title', 'vision', 'mission', 'service_product', 'Webpage_logo', 'Webpage_url', 'Sub')
    icon = '<i class="material-icons">view_module</i>'
    list_display = ('title', 'Webpage_url')
    search_fields = ('title', 'Webpage_url',)

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def save_formset(self, request, form, formset, change):
        formset.save()

    def get_queryset(self, request):
        qs = super(WebpageAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user_id=request.user.id)


class FestAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">view_module</i>'

    def get_queryset(self, request):
        qs = super(FestAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(webpage__user_id=request.user.id)

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        if db_field.name == 'webpage':
            if request.user.is_superuser:
                kwargs['queryset'] = Webpage.objects.all()
            else:
                kwargs['queryset'] = Webpage.objects.filter(user_id=request.user)
        else:
            pass
        return super(FestAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


class MemberInline(admin.StackedInline):
    model = Member
    can_delete = True
    verbose_name_plural = 'member'


class UserAdmin(BaseUserAdmin):
    inlines = (MemberInline,)


admin.site.unregister(User)
admin.site.register(model.User, UserAdmin)
admin.site.register(model.Webpage, WebpageAdmin)
admin.site.register(model.Category)
admin.site.register(model.SubCategory)
admin.site.register(model.Festival, FestAdmin)
admin.site.site_header = ' لینک بوک '
admin.site.site_title = 'قلعه وب'
