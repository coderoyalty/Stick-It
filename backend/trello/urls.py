from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from rest_framework_simplejwt import views as jwt_views
from users.views import Me, RegisterUser
from boards.views import NotificationList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterUser.as_view(), name='register'),
    path('token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('projects/', include('projects.urls')),
    path('boards/', include('boards.urls')),
    path('me/', Me.as_view(), name="me"),
    path('notifications/', NotificationList.as_view(), name="notification-list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
