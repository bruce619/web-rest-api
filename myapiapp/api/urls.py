from django.urls import path, include
from .views import (
    api_detail_project_view,
    api_update_project_view,
    api_delete_project_view,
    api_create_project_view,
    api_all_project_view,

    api_detail_action_project_view,
    api_detail_action_project_id_view,
    api_detail_action_view,
    api_update_action_view,
    api_delete_action_view,
    api_create_action_view,
    api_all_action_view,



)

app_name = 'myapiapp'

urlpatterns = [
    path('projects', api_create_project_view, name='project-create'),
    path('projects', api_all_project_view, name='project-list'),
    path('projects/<projectid>', api_detail_project_view, name='project-detail'),
    path('projects/<projectid>', api_update_project_view, name='project-update'),
    path('projects/<projectid>', api_delete_project_view, name='project-delete'),

    path('projects/<projectid>/actions', api_create_action_view, name='action-create'),
    path('actions', api_all_action_view, name='action-list'),
    path('projects/<projectid>/actions', api_detail_action_project_view, name='action-project-detail'),
    path('actions/<actionid>', api_detail_action_view, name='action-detail'),
    path('projects/projects/<projectid>/actions/<actionid>', api_detail_action_project_id_view, name='action-id-detail'),
    path('projects/projects/<projectid>/actions/<actionid>', api_update_action_view, name='action-update'),
    path('projects/projects/<projectid>/actions/<actionid>', api_delete_action_view, name='action-delete'),


]