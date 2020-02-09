from rest_framework import serializers
from myapiapp.models import Projects, Actions


class ProjectSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ProjectSerializer, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = True
        self.fields['description'].required = True

    class Meta:
        model = Projects
        fields = '__all__'


class ActionSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ActionSerializer, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['project-id'].required = True
        self.fields['description'].required = True
        self.fields['note'].required = True

    class Meta:
        model = Actions
        fields = '__all__'



