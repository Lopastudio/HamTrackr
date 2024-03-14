from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings  # Import settings module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logbook.urls')),
]

# Serve static files during development
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
