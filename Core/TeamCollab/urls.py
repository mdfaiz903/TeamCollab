from django.urls import path,include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register('users',views.UserViewSet)
router.register('projects',views.ProjectViewSet)
router.register('projectsmember',views.ProjectMemberViewSet)
router.register('task',views.TaskViewSet)
router.register('comment',views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/register/', views.RegisterUserView.as_view(), name='register-user'),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('projects/<int:project_id>/tasks/', views.ProjectTaskListCreateView.as_view(), name='project-tasks'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]