from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.pagination import PageNumberPagination
from myapiapp.models import Project, Action
from myapiapp.api.serializers import ProjectSerializer, ActionSerializer


# get all project and create a project
@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_create_project_api_view(request):

    if request.method == 'GET':
        project = Project.objects.all().order_by("-created_at")
        serializer = ProjectSerializer(project, many=True)
        return JsonResponse({'projects': serializer.data}, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        user = request.user
        project = Project(user=user)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'project': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


# retrieve a single project, update a project, delete a project
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_update_delete_project_api_view(request, project_id=None):

    if request.method == 'GET':
        try:
            project = Project.objects.filter(id=project_id).order_by("-created_at")
        except Project.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(project, many=True)
        return JsonResponse({'project': serializer.data}, safe=False, status=status.HTTP_200_OK)

    try:
        project = Project.objects.get(id=project_id).order_by("-created_at")
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    owner = Project.objects.filter(user=user)
    if not owner:
        return Response({'Response': "You do not have the permission to edit / delete this"})

    if request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'project': serializer.data}, safe=False, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PATCH':
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'project': serializer.data}, safe=False, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return JsonResponse({'success': "successfully deleted"}, status=status.HTTP_204_NO_CONTENT)

# ###########################################################


# Get an action, Create a action
@api_view(['GET', 'POST'])
@csrf_exempt
@permission_classes((IsAuthenticated,))
def get_create_action_api_view(request, project_id=None):

    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        actions = Action.objects.filter(project=project).distinct().order_by("-created_at")
        serializer = ActionSerializer(actions, many=True)
        return JsonResponse({'actions': serializer.data}, safe=False, status=status.HTTP_200_OK)

    user = request.user
    owner = project.user

    if user != owner:
        return Response({'Response': "You do not have the permission to create an action for this project"})

    if request.method == 'POST':
        actions = Action(user=owner, project=project)
        serializer = ActionSerializer(actions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'action': serializer.data}, safe=False, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# retrieve all actions
@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_all_action_api_view(request):
    try:
        action = Action.objects.all().order_by("-created_at")
    except Action.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActionSerializer(action, many=True)
        return JsonResponse({"actions": serializer.data}, safe=False, status=status.HTTP_200_OK)


# retrieve a single action
@api_view(['GET'])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_single_action_api_view(request, action_id=None):
    try:
        action = Action.objects.filter(id=action_id).order_by("-created_at")
    except Action.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ActionSerializer(action, many=True)
        return JsonResponse({"action": serializer.data}, safe=False, status=status.HTTP_200_OK)


# get, update, delete action
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated,))
def get_update_delete_action_api_view(request, action_id, project_id):

    if request.method == 'GET':
        try:
            action = Action.objects.filter(id=action_id, project=project_id)
        except Action.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = ActionSerializer(action, many=True)
            return JsonResponse({"action": serializer.data}, safe=False, status=status.HTTP_200_OK)

    try:
        action = Action.objects.get(id=action_id, project=project_id)
    except Project.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    project = Project.objects.get(id=project_id)

    if project.user != user and action.user != user:
        return Response({'Response': 'You do not have the permission to edit / delete this'})

    if request.method == 'PUT':
        serializer = ActionSerializer(action, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'action': serializer.data}, safe=False, status=status.HTTP_200_OK)
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        action.delete()
        return JsonResponse({'success': "successfully deleted"}, status=status.HTTP_204_NO_CONTENT)


