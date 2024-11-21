from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenVerifyView,TokenRefreshView,)


urlpatterns = [
    path('admin/', admin.site.urls),

    # User Management
    path('api/user-management/', include('user_management.urls')),
    # Student Management
    path('api/student-management/', include('student_management.urls')),
    # Teacher Management
    path('api/teacher-management/', include('teacher_management.urls')),
    # Parent Portal
    path('api/parent-portal/', include('parent_portal.urls')),
    # Academic Management
    path('api/academic-management/', include('academic_management.urls')),
    # Attendance Management
    path('api/attendance-management/', include('attendance_management.urls')),
    # Fee Management
    path('api/fee-management/', include('fee_management.urls')),
    # Library Management
    path('api/library-management/', include('library_management.urls')),
    # Transport Management
    path('api/transport-management/', include('transport_management.urls')),
    # Notifications
    path('api/notifications/', include('notifications.urls')),
    # Reports & Analytics
    path('api/reports-analytics/', include('reports_analytics.urls')),
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
