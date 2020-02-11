from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from myapiapp.models import Projects, Actions
from myapiapp.api.serializers import ProjectSerializer, ActionSerializer


# retrieve a a single project, update a project, delete a project
@api_view(['GET', 'PUT', 'DELETE', ])
@permission_classes((IsAuthenticated,))
def api_get_update_delete_project_view(request, projectid):
    try:
        project = Projects.objects.get(slug=projectid)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if project.user != user:
        return Response({'Response': 'You do not have the permission to edit this'})

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Update Successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation = project.delete()
        data = {}
        if operation:
            data['success'] = 'successful delete'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)


# update a project

#  create a project, get all projects
@api_view(['GET', 'POST', ])
@permission_classes((IsAuthenticated,))
def api_get_create_project_view(request):

    if request.method == 'GET':
        project = Projects.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user = request.user
        project = Projects(user=user)
        serializer = ProjectSerializer(project, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


###########################################################


# retrieve all actions
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_all_action_view(request):
    try:
        action = Actions.objects.all()
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProjectSerializer(action)
        return Response(serializer.data)


# retrieve a single action
@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_single_action_view(request, actionid):
    try:
        action = Actions.objects.get(slug=actionid)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActionSerializer(action)
        return Response(serializer.data)


# get, update, delete action
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def api_get_update_delete_action_view(request, actionid, projectid):
    try:
        action = Actions.objects.get(slug=actionid)
        project = Projects.objects.get(slug=projectid)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user

    if project.user != user and action.user != user:
        return Response({'Response': 'You do not have the permission to edit this'})

    if request.method == 'GET':
        if request.method == 'GET':
            serializer = ActionSerializer(action, project)
            return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ActionSerializer(action, request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Update Successful'
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        operation = action.delete()
        data = {}
        if operation:
            data['success'] = 'successful delete'
        else:
            data['failure'] = 'delete failed'
        return Response(data=data)


# Get an action, Create a action
@api_view(['GET', 'POST', ])
@permission_classes((IsAuthenticated,))
def api_get_create_action_view(request, projectid):
    try:
        project = Projects.objects.get(slug=projectid)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    action = Actions(user=user)

    if request.method == 'GET':
        serializer = ActionSerializer(project)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ActionSerializer(action, data=request.data)
        data = {}
        if serializer.is_valid():
            action = serializer.save(commit=False)
            action.project = project
            action.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


