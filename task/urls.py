from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListCreateAPIView.as_view()),
    # path('task/<int:id>/', views.task_item_update_delete_api_view),
    path('tasks/<int:id_task>/', views.TaksDeteilAPIView.as_view()),
]