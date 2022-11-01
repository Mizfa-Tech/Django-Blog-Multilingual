from django.urls import path, include
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('create/', views.CreatePostView.as_view(), name='create'),
    path('<pk>/', views.PostDetailView.as_view(), name='detail'),
    path('update/<pk>/', views.UpdatePostView.as_view(), name='update'),
]
