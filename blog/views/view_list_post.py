from django.views import generic
from blog.models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/list_post.html'
    context_object_name = "posts"

    def get_queryset(self):
        query = self.model.objects.filter(is_active=True)
        return query
