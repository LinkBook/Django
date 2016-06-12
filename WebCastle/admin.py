# Register your models here.
from django.contrib import admin

import WebCastle.models as model

# Register your models here.
from WebCastle import models


class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email',)
    list_display = ('name', 'message', 'email')


class KarbarAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email')
    search_fields = ('username',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_name', 'comment_email', 'comment')
    search_fields = ('comment_name', 'comment_email',)


# class Person(models.Model):
#     first_name = models.CharField(max_length=50)
#     color_code = models.CharField(max_length=6)
#
#     def colored_first_name(self):
#         return '<span style="color: #%s;">%s</span>' % (
#             self.color_code, self.first_name)
#
#     colored_first_name.allow_tags = True
#     colored_first_name.admin_order_field = 'first_name'
#     colored_first_name.short_description = 'first name'
#
#
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'colored_first_name')

# class ModelOptions(admin.ModelAdmin):
#     fieldsets = (
#         ('', {
#             'fields': ('title', 'subtitle', 'slug', 'pub_date', 'status',),
#         }),
#         ('Flags', {
#             'classes': ('grp-collapse grp-closed',),
#             'fields': ('flag_front', 'flag_sticky', 'flag_allow_comments', 'flag_comments_closed',),
#         }),
#         ('Tags', {
#             'classes': ('grp-collapse grp-open',),
#             'fields': ('tags',),
#         }),
#     )
#
#
# class StackedItemInline(admin.StackedInline):
#     classes = ('grp-collapse grp-open',)
#
#
# class TabularItemInline(admin.TabularInline):
#     classes = ('grp-collapse grp-open',)


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
admin.site.site_title = 'قلعه وب'
