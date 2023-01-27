from rest_framework import generics as rest_generic_views, permissions, exceptions as rest_exceptions

from to_do.api_todos.models import Todo, Category
from to_do.api_todos.serializers import TodoCreateSerializer, TodoListSerializer, CategorySerializer, \
    TodoDetailsSerializer


class ListCreateTodoApiView(rest_generic_views.ListCreateAPIView):
    queryset = Todo.objects.all()
    # add two serializers to this view
    create_serializer_class = TodoCreateSerializer
    list_serializer_class = TodoListSerializer
    filter_names = ('category',)

    # only authenticated users can view this
    permission_classes = (
        permissions.IsAuthenticated,
    )

    # use list_serializer_class or create_serializer_class
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return self.list_serializer_class
        return self.create_serializer_class

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        # simple add filter to the queryset
        # category_id = self.request.query_params.get('category', None)
        # if category_id:
        #     queryset = queryset.filter(category=category_id)
        # return queryset
        return self.__apply_filters_to_queryset(queryset)

    def __apply_filters_to_queryset(self, queryset):
        queryset_params = {}
        for filter_name in self.filter_names:
            filter_id = self.request.query_params.get(filter_name, None)
            if filter_id:
                queryset_params[f'{filter_name}'] = filter_id

        return queryset.filter(**queryset_params)


class DetailsTodoApiView(rest_generic_views.RetrieveUpdateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoDetailsSerializer

    permission_classes = (
        permissions.IsAuthenticated,
    )

    def get_object(self):
        todo = super().get_object()
        if todo.user != self.request.user:
            raise rest_exceptions.PermissionDenied
        return todo


class ListCategoriesApiView(rest_generic_views.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    # show only user categories
    def get_queryset(self):
        return self.queryset.filter(todo__user_id=self.request.user.id).distinct()
