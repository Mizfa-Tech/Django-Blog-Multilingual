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
        (_('Fa'), {'fields': ('title_fa', 'category_fa', 'content_fa', 'is_active_fa')}),
        (_('En'), {'fields': ('title_en', 'category_en', 'content_en', 'is_active_en')}),
        (_("Main"), {'fields': ('thumbnail', 'thumbnail_alt', 'slug', 'author',)}),
        (_("Date"), {'fields': ('created_at', "updated_at")}),
        (_("SEO information"), {'fields': ("meta_title", "meta_description")}),
        (_('Settings'), {'fields': ('status',)}),
    )

    add_fieldsets = (
        (_('Fa'), {'fields': ('title_fa', 'category_fa', 'content_fa', 'is_active_fa')}),
        (_('En'), {'fields': ('title_en', 'category_en', 'content_en', 'is_active_en')}),
        (_("Main"), {'fields': ('thumbnail', 'thumbnail_alt', 'slug', 'author',)}),
        (_("SEO information"), {'fields': ("meta_title", "meta_description")}),
        (_('Settings'), {'fields': ('status',)}),
    )
