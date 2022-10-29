from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', "author", 'slug', 'status', 'created_at', 'updated_at')
    search_fields = ('title', 'slug', 'author')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ("Main", {'fields': ('title', 'slug', 'author', 'category', 'content')}),
        ("Date", {'fields': ('created_at', "updated_at")}),
        ("SEO information", {'fields': ("meta_title", "meta_description")}),
        ('Settings', {'fields': ('status',)}),
    )

    add_fieldsets = (
        ("Main", {'fields': ('title', 'slug', 'author', 'category', 'content')}),
        ("SEO Information", {'fields': ("meta_title", "meta_description")}),
        ('Settings', {'fields': ('status',)}),
    )