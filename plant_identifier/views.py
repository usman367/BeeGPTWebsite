from urllib import request

from django.shortcuts import render
from django.template import context

from .forms import PlantImageForm
from .models import PlantImage

# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            plant_image = form.save()
            return render(request, 'image_upload/image_result.html', {'plant_image': plant_image})
    else:
        form = PlantImageForm()
    return render(request, 'image_upload/home.html', {'form': form})


# Created a new view function for the biodiversity page
def biodiversity(request):
    return render(request, 'image_upload/biodiversity.html')
