from django.views import generic
from blog.models import Post
from django.utils.translation import gettext as _
from blog.forms import CreateUpdatePostForm


class CreatePostView(generic.CreateView):
    model = Post
    form_class = CreateUpdatePostForm
    template_name = 'blog/create_Update_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['view_title'] = _('create post')
        return context

    def get_success_url(self):
        pass
