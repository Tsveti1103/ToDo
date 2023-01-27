from django.urls import path

from to_do.api_todos.views import ListCreateTodoApiView, ListCategoriesApiView, DetailsTodoApiView

urlpatterns = (
    path('', ListCreateTodoApiView.as_view(), name='api list todos'),
    path('categories/', ListCategoriesApiView.as_view(), name='api list categories'),
    path('<int:pk>/', DetailsTodoApiView.as_view(), name='api details todo'),
)