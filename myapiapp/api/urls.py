from django.urls import path
from .views import (
    get_create_project_api_view,
    get_update_delete_project_api_view,
    get_create_action_api_view,
    get_all_action_api_view,
)


urlpatterns = [
    path('projects/', get_create_project_api_view, name='get-create-project'),
    path('projects/<int:id>/', get_update_delete_project_api_view, name='project-update-delete'),
    path('projects/<int:id>/actions/', get_create_action_api_view, name='get-action-project'),
    path('actions/', get_all_action_api_view, name='get-action'),
#
#     path('projects/<projectid>/actions', api_get_create_action_view, name='action-get_create'),
#     path('actions', api_all_action_view, name='action-list'),
#     path('actions/<actionid>', api_single_action_view, name='action-single-action'),
#     path('projects/projects/<projectid>/actions/<actionid>', api_get_update_delete_action_view, name='action-get-update-delete-action'),
#
]
