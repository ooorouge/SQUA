from django.urls import path
from myclasses import views

urlpatterns = [
    path('', views.listRequested),
    path(r'/del[0-9]+', views.classDelete)
]