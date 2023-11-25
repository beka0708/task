from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Task
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import TaskSerializer, TaskValidateSerializer, TaskItemSerializer


class TaskListCreateAPIView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def create(self, request, *args, **kwargs):
        serializer = TaskValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={'errors': serializer.errors})

        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        completed = serializer.validated_data.get('completed')

        task = Task.objects.create(title=title, description=description, completed=completed)

        return Response(data=TaskItemSerializer(task).data,
                        status=status.HTTP_201_CREATED)


class TaksDeteilAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_field = 'id_task'

    def put(self, request, *args, **kwargs):
        try:
            item = Task.objects.get(id_task=kwargs['id_task'])
        except Task.DoesNotExist:
            return Response(data={'error': 'Tasks not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskValidateSerializer(instance=item, data=request.data)
        task = Task.objects.all()
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        task.title = serializer.validated_data.get('title')
        task.description = serializer.validated_data.get('description')
        task.completed = serializer.validated_data.get('completed')
        return Response(data=TaskSerializer(item).data, status=status.HTTP_200_OK)


# @api_view(['GET', 'PUT', 'DELETE'])
# def task_item_update_delete_api_view(request, id):
#     try:
#         task = Task.objects.get(id=id)
#     except Task.DoesNotExist:
#         return Response(data={'error': 'Task not found'},
#                         status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         data = TaskItemSerializer(instance=task, many=False).data
#         return Response(data=data)
#     elif request.method == 'DELETE':
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     else:
#         serializer = TaskValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         task.title = serializer.validated_data.get('title')
#         task.description = serializer.validated_data.get('description')
#         task.completed = serializer.validated_data.get('completed')
#         return Response(data=TaskItemSerializer(task).data,
#                         status=status.HTTP_202_ACCEPTED)
