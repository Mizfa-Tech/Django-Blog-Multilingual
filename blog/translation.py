from modeltranslation.translator import register, TranslationOptions
from blog.models import Post, Category


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("title", "description", 'parent_category')


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ("title", "content", 'category')
