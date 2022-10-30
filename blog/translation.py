from modeltranslation.translator import register, TranslationOptions
from blog.models import Post, Category


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = (
        'meta_title', 'meta_description', 'created_at', 'updated_at',
        'created_at_jalali', 'updated_at_jalali', "title", "content",
        "slug", "author", "thumbnail", "thumbnail_alt", 'status', 'category',
    )


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'meta_title', 'meta_description', 'created_at', 'updated_at',
        'created_at_jalali', 'updated_at_jalali', "title", "description",
        "slug", "thumbnail", "thumbnail_alt", 'status', 'parent_category'
    )
