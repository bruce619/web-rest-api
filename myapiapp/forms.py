from django import forms
from .models import Projects, Actions


class CreateProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CreateProjectForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = True
        self.fields['description'].required = True

    class Meta:
        model = Projects
        fields = ['name', 'description', 'completed']
        exclude = ('user',)

    def is_valid(self):
        valid = super(CreateProjectForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        project = super(CreateProjectForm, self).save(commit=False)
        if commit:
            project.save()
        return project


class CreateActionForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(CreateActionForm, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['project_id'].required = True
        self.fields['description'].required = True
        self.fields['note'].required = True

    class Meta:
        model = Actions
        fields = ['project_id', 'description', 'note']
        exclude = ('user',)

    def is_valid(self):
        valid = super(CreateActionForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        action = super(CreateActionForm, self).save(commit=False)
        if commit:
            action.save()
        return action

