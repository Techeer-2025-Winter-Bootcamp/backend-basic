from django.urls import path

from user.views import SignUpView, LoginView

app_name = 'user'

urlpatterns = [
    path('users/signup', SignUpView.as_view(), name='signup'),
    path('users/login', LoginView.as_view(), name='login'),
]
