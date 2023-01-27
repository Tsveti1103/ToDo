from django.urls import path

from to_do.api_auth.views import RegisterApiView, LoginApiView, LogoutApiView

urlpatterns = (
    path('register/', RegisterApiView.as_view(), name='api register user'),
    path('login/', LoginApiView.as_view(), name='api login user'),
    path('logout/', LogoutApiView.as_view(), name='api logout user'),
)
