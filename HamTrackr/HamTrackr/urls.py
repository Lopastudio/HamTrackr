from django.contrib import admin
from django.urls import path, include  # Add include import to include our app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('logbook.urls')),  # Include our logbook app URLs
]
