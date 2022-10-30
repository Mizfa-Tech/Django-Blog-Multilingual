from django.views import generic
from blog.models import Post


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/detail_post.html'
    context_object_name = "post"
