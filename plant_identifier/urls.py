from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('biodiversity/', views.biodiversity, name='biodiversity'),
    path('tutorial/', views.tutorial, name='tutorial')
]
