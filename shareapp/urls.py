
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # 👇 this fixes your issue
    path('account/', views.account, name='account'),

    path('upload/', views.upload_file, name='upload'),
    path('processing/', views.processing, name='processing'),
    path('result/', views.qr_result, name='result'),
    path('download/<str:filename>/', views.download_file, name='download'),
]
