from rest_framework import serializers
from myapiapp.models import Projects, Actions


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=120)
    description = serializers.CharField()
    completed = serializers.BooleanField(default=False)
    username = serializers.SerializerMethodField('get_username_from_user')

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ProjectSerializer, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['name'].required = True
        self.fields['description'].required = True

    class Meta:
        model = Projects
        fields = ['name', 'description', 'completed', 'username']

    def get_username_from_user(self, project):
        username = project.user.username
        return username


class ActionSerializer(serializers.ModelSerializer):
    project_id = serializers.IntegerField()
    description = serializers.CharField()
    note = serializers.CharField()
    username = serializers.SerializerMethodField('get_username_from_user')

    def __init__(self, *args, **kwargs):
        # first call parent's constructor
        super(ActionSerializer, self).__init__(*args, **kwargs)
        # there's a `fields` property now
        self.fields['project_id'].required = True
        self.fields['description'].required = True
        self.fields['note'].required = True

    class Meta:
        model = Actions
        fields = ['project_id', 'description', 'note', 'username']

    def get_username_from_user(self, action):
        username = action.user.username
        return username



