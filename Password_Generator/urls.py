from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('password.urls')),
    path('password/', include('password.urls')),
]
