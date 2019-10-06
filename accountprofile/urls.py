from django.urls import path, re_path
from accountprofile import views

urlpatterns = [
    path('', views.listRequested),
    path('edit', views.listRequested, name='profedit')
]