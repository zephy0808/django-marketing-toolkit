from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListView.as_view(), name='preview'),
]
