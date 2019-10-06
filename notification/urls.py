from django.urls import path, re_path
from notification import views

urlpatterns = [
    path('', views.notification_requested),
    re_path(r'read/', views.read_nofitication, name='globalread'),
    re_path(r'accept/', views.read_nofitication),
    re_path(r'decline/', views.read_nofitication),
]