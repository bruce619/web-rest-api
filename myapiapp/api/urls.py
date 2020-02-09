from django.urls import path, include
from rest_framework import routers
from .views import ProjectsViewSet, ActionsViewSet

router = routers.DefaultRouter()
router.register('projects', ProjectsViewSet)
router.register('actions', ActionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]