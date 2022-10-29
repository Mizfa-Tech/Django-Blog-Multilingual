from django.views import generic
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/list_post.html'
    context_object_name = "posts"

