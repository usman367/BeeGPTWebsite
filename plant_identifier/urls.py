from django.urls import path
from . import views


# Set up the project routing
# Map each url to its corresponding view function
urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('biodiversity/', views.biodiversity, name='biodiversity'),
    path('tutorial/', views.tutorial, name='tutorial')
]
