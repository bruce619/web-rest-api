from rest_framework import serializers
from myapiapp.models import Project, Action


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'user', 'name', 'description', 'completed', 'created_at']
        read_only_fields = ('id', 'user', 'created_at',)


class ActionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Action
        fields = ['id', 'user', 'project', 'description', 'note', 'created_at']
        read_only_fields = ('id', 'user', 'project', 'created_at',)



