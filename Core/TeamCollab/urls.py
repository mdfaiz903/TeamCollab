from django.urls import path,include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register('users',views.UserViewSet)
router.register('projects',views.ProjectViewSet)
router.register('projectsmember',views.ProjectMemberViewSet)
router.register('task',views.TaskViewSet)
router.register('comment',views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/register/', views.RegisterUserView.as_view(), name='register-user'),
    path('users/login/', views.LoginUserView.as_view(), name='login-user'),
    path('projects/<int:project_id>/tasks/', views.ProjectTaskListCreateView.as_view(), name='project-tasks'),
]