from django.contrib import admin
from django.urls import path
from . import views  # If you have views to import, otherwise, you can remove it

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),

    # Example of a home page or index page (replace with your actual views)
    path('', views.home, name='home'),

    # Add any other URL patterns for your apps here:
    # path('some-url/', views.some_view, name='some_name'),
]

# Serve static and media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
