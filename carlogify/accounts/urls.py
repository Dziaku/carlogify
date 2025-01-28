from django.urls import path

from .views import SignUpView

app_name = 'users'
urlpatterns = [
    path('register/', SignUpView.as_view(), name='register')
]