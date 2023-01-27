from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include([
        path('auth/', include('to_do.api_auth.urls')),
        path('todos/', include('to_do.api_todos.urls'))
    ]))
]
