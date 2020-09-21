from django.urls import path
from .views import (
    get_create_project_api_view,
    get_update_delete_project_api_view,
    get_create_action_api_view,
    get_all_action_api_view,
    get_single_action_api_view
)


urlpatterns = [
    path('projects/', get_create_project_api_view, name='get-create-project'),
    path('projects/<int:project_id>/', get_update_delete_project_api_view, name='project-update-delete'),
    path('projects/<int:project_id>/actions/', get_create_action_api_view, name='get-action-project'),
    path('actions/', get_all_action_api_view, name='get-action'),
    path('actions/<int:action_id>/', get_single_action_api_view, name='get-single-action'),


]
