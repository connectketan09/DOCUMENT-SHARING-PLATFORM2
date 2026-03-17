
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('upload/', views.upload_file),
    path('processing/', views.processing),
    path('result/', views.qr_result),
    path('download/<str:filename>/', views.download_file),
]