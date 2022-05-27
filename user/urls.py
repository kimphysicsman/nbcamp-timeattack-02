from django.urls import path
from . import views

urlpatterns = [
    path('register', views.sign_up_view, name='sign-up'),
]