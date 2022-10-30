from django.contrib import admin
from blog.models import Category
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('title', "parent_category", 'slug', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'parent_category')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (_("Main"), {'fields': ('title', 'slug', 'thumbnail', 'thumbnail_alt', 'description')}),
        (_('Sub Category'), {'fields': ('parent_category',)}),
        (_('Date'), {'fields': ('created_at', "updated_at")}),
        (_("SEO Information"), {'fields': ("meta_title", "meta_description")}),
        (_('Settings'), {'fields': ('status',)}),
    )

    add_fieldsets = (
        (_("Main"), {'fields': ('title', 'slug', 'thumbnail', 'thumbnail_alt', 'description')}),
        (_('Sub Category'), {'fields': ('parent_category',)}),
        (_("SEO Information"), {'fields': ("meta_title", "meta_description")}),
        (_('Settings'), {'fields': ('status',)}),
    )
