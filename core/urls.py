from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# ----------------------------------------------------------------------------------------------------------------------
urlpatterns_api_v1 = [

]

urlpatterns_app = [

]
# ----------------------------------------------------------------------------------------------------------------------
urlpatterns = [
    # URL Admin App
    path('admin/', admin.site.urls),

    # URL Api Apps
    path('api/v1/', include(urlpatterns_api_v1)),

    # URL Apps
    path('', include(urlpatterns_app)),

    # URL Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# -------------------------------------- Config Static ----------------------------------------------------------------
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
