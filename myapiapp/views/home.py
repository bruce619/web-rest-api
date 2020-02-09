from ..models import Projects, Actions
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin


# List view for all Project
class ProjectListView(ListView):
    model = Projects
    template_name = 'project_listing.html'
    context_object_name = 'projects'
    ordering = ['-id']
    paginate_by = 4


# Detail view of Project
class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'project_details.html'
    context_object_name = 'projects'
    pk_url_kwarg = 'id'

