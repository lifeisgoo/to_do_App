from django.urls import path
from .views import TaskViews, ToDoModelView

urlpatterns = [
    path('', TaskViews.as_view()),
    path('tasks/', ToDoModelView.as_view()),
]