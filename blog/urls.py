from django.urls import path, include
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.PostListView.as_view(), name='list'),
    path('<pk>/', views.PostDetailView.as_view(), name='detail'),
]
