from django.shortcuts import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from ..models import Project
from ..forms import CreateProjectForm
from django.contrib.auth.decorators import login_required
import sweetify


# create a project
class CreateProjectView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = CreateProjectForm
    template_name = 'project.html'
    success_url = reverse_lazy('project-listing')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(CreateProjectView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            sweetify.success(self.request, title='Successfully created job!',
                             text='You have successfully created a Project', icon='success', button="OK", timer=3000)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# update a project
class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['name', 'description', 'completed']
    template_name = 'project_update_form.html'
    pk_url_kwarg = 'id'

    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        return form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        project = self.get_object()
        if self.request.user == project.user:
            return True
        return False

    def get_success_url(self):
        return reverse_lazy('project-detail', kwargs={'id': self.kwargs['id']})


# Delete a Post
class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'project_confirm_delete.html'
    success_url = reverse_lazy('project-listing')

    def test_func(self):
        project = self.get_object()
        # Only users that created the post are permitted to delete the post
        if self.request.user == project.user:
            return True
        return False


@login_required(login_url=reverse_lazy('login'))
def completed(request, project_id=None):
    # Gets the the project posted by the logged in user
    project = Project.objects.get(user_id=request.user.id, id=project_id)
    # Mark as filled
    project.completed = True
    project.save()
    return HttpResponseRedirect(reverse_lazy('project-listing'))

