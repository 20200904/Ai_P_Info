from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_and_analyze_pdf, name='upload_pdf'),
]
