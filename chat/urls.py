from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_document, name='upload'),
    path('chat/', views.chat, name='chat'),
]
