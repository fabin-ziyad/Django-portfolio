
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.site.site_header = 'Fabin Ziyad [ Admin Panel ]'
urlpatterns = [
    path('', include('feeds.urls')),
    path('ownerlogin/', admin.site.urls),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
