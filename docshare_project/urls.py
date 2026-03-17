from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shareapp.urls')),
]

# 🔥 MEDIA SERVING (CRITICAL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)