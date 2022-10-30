from rest_framework import routers
from blog.api import viewset

router = routers.DefaultRouter()
router.register('category', viewset.CategoryViewSet, basename='category')
router.register('', viewset.PostViewSet, basename='post')

urlpatterns = router.urls
