from django.urls import path
from .views import (
    api_get_create_project_view,
    api_get_update_delete_project_view,


    api_get_create_action_view,
    api_get_update_delete_action_view,
    api_single_action_view,
    api_all_action_view,



)

app_name = 'myapiapp'

urlpatterns = [
    path('projects', api_get_create_project_view, name='project-get-create'),
    path('projects/<projectid>', api_get_update_delete_project_view, name='project-get-update-delete'),

    path('projects/<projectid>/actions', api_get_create_action_view, name='action-get_create'),
    path('actions', api_all_action_view, name='action-list'),
    path('actions/<actionid>', api_single_action_view, name='action-single-action'),
    path('projects/projects/<projectid>/actions/<actionid>', api_get_update_delete_action_view, name='action-get-update-delete-action'),

]