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
        (_('Fa'), {'fields': ('title_fa', 'parent_category_fa', 'description_fa', 'is_active_fa')}),
        (_('En'), {'fields': ('title_en', 'parent_category_en', 'description_en', 'is_active_en')}),
        (_("Main"), {'fields': ('slug', 'thumbnail', 'thumbnail_alt')}),
        (_('Date'), {'fields': ('created_at', "updated_at")}),
        (_("SEO Information"), {'fields': ("meta_title", "meta_description")}),
        (_('Settings'), {'fields': ('status',)}),
    )

    add_fieldsets = (
        (_('Fa'), {'fields': ('title_fa', 'parent_category_fa', 'description_fa', 'is_active_fa')}),
        (_('En'), {'fields': ('title_en', 'parent_category_en', 'description_en', 'is_active_en')}),
        (_("Main"), {'fields': ('slug', 'thumbnail', 'thumbnail_alt')}),
        (_("SEO Information"), {'fields': ("meta_title", "meta_description")}),
        (_('Settings'), {'fields': ('status',)}),
    )
