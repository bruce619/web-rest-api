from django.urls import path, include
from django.views.generic import TemplateView
from .views.project import CreateProjectView, ProjectUpdateView, ProjectDeleteView, completed
from .views.action import CreateActionsView, ActionUpdateView, ActionDeleteView
from .views.home import ProjectListView, ProjectDetailView


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('project/create/', CreateProjectView.as_view(), name='project-create'),
    path('project/<int:id>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('project-list/', ProjectListView.as_view(), name='project-listing'),
    path('project-detail/<int:id>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('project-completed/<int:project_id>', completed, name='projects-completed'),
    path('project/<int:project_id>/action/', CreateActionsView.as_view(), name='create-action'),
    path('action/<int:id>/update/', ActionUpdateView.as_view(), name='action-update'),
    path('action/<int:pk>/remove/', ActionDeleteView.as_view(), name='action-delete'),


]
