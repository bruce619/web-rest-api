from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission, IsAdminUser, IsAuthenticatedOrReadOnly
from myapiapp.models import Projects, Actions
from myapiapp.api.serializers import ProjectSerializer, ActionSerializer


class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Projects.objects.all()


class ActionsViewSet(viewsets.ModelViewSet):
    serializer_class = ActionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Actions.objects.all()


