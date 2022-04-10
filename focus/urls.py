
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from website.views import ChangePasswordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('password-change/', ChangePasswordView.as_view(), name='password_change'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
