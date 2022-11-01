from blog.models import Post
from modeltranslation.forms import TranslationModelForm


class CreateUpdatePostForm(TranslationModelForm):
    class Meta:
        model = Post
        fields = '__all__'
