from django.urls import path, include

app_name = 'blog_api'
urlpatterns = [
    path('', include('blog.api.router'))
]
