from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pharmanic_app.urls')),
    path('', include('pwa.urls')),
    path('', include('pwa_webpush.urls')),
]
