from django.urls import path
from . import views
from .views import upload_image

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('biodiversity/', views.biodiversity, name='biodiversity')
]
