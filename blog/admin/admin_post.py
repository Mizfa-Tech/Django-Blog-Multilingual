from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from blog.models import Post


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    list_display = ('title', "author", 'slug', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'author')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_("Main"), {'fields': ('title', 'slug', 'author', 'category', 'content')}),
        (_("Date"), {'fields': ('created_at', "updated_at")}),
        (_("SEO information"), {'fields': ("meta_title", "meta_description")}),
        (_('Settings'), {'fields': ('status',)}),
    )

    add_fieldsets = (
        (_("Main"), {'fields': ('title', 'slug', 'author', 'category', 'content')}),
        (_("SEO information"), {'fields': ("meta_title", "meta_description")}),
        (_('Settings'), {'fields': ('status',)}),
    )
