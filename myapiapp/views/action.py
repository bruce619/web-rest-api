# from django.shortcuts import render, redirect, HttpResponseRedirect
# from ..models import Project, Action
# from django.shortcuts import get_object_or_404
# from ..forms import CreateActionForm
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.urls import reverse_lazy
# from django.views.generic import CreateView, UpdateView, DeleteView
# import sweetify
#
#
# # create action
# class CreateActionsView(LoginRequiredMixin, CreateView):
#     model = Action
#     form_class = CreateActionForm
#     slug_field = 'project_id'
#     slug_url_kwarg = 'project_id'
#     template_name = 'action.html'
#     success_url = reverse_lazy('project-listing')
#
#     def post(self, request, *args, **kwargs):
#         form = self.get_form()
#         if form.is_valid():
#             sweetify.success(self.request, title='Successfully Applied',
#                              text='You have successfully created an action', icon='success', button='Close',
#                              timer=3000)
#             return self.form_valid(form)
#         else:
#             sweetify.error(self.request, title='Error',
#                            text='Unsuccessful, try again',
#                            icon='error', button='Close', timer=5000)
#             return HttpResponseRedirect(reverse_lazy('project-detail', kwargs={'id': self.kwargs['project_id']}))
#
#     def form_valid(self, form):
#         project = get_object_or_404(Project, id=self.kwargs['project_id'])
#         form.instance.user = self.request.user
#         action = form.save(commit=False)
#         action.project = project
#         action.save()
#         return super(CreateActionsView, self).form_valid(form)
#
#     def test_func(self):
#         project = get_object_or_404(Project, id=self.kwargs['project_id'])
#         # Only users that created the project are permitted to create an action
#         if self.request.user == project.user:
#             return True
#         return False
#
#
# # update a action
# class ActionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Action
#     fields = ['description', 'note']
#     template_name = 'action.html'
#     pk_url_kwarg = 'id'
#     success_url = reverse_lazy('project-listing')
#
#     def get_form(self, **kwargs):
#         form = super().get_form(**kwargs)
#         return form
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         action = self.get_object()
#         if self.request.user == action.user:
#             return True
#         return False
#
#
# # Delete a action
# class ActionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Action
#     template_name = 'action_confirm_delete.html'
#     success_url = reverse_lazy('project-listing')
#
#     def test_func(self):
#         project = self.get_object()
#         # Only users that created the post are permitted to delete the post
#         if self.request.user == project.user:
#             return True
#         return False
#
#
#
#
#
#
#
#
