from django.shortcuts import render
from openai import OpenAI
from .forms import PlantImageForm
import requests


# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            plant_image = form.save()

            # Call to PlanetNet API
            api_url = 'https://my-api.plantnet.org/v2/identify/all'
            api_key = '2b10kJ93KxHKQXXnSGKDxuRpfe'
            files = {'images': plant_image.image}
            client = OpenAI(
                api_key="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"
            )
            plant_info = ""

            response = requests.post(api_url, files=files, headers={'Authorization': f'Bearer {api_key}'})
            if response.status_code == 200:
                data = response.json()
                # The API returns a field 'species' with the species name
                common_name = data["results"][0]["species"]["commonNames"][0]
                plant_image.species = common_name
                plant_image.save()

                try:
                    prompt = f"Provide information about the biodiversity and ecosystem of the {plant_image.species}."
                    response = client.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": prompt}]
                    )
                    plant_info = response.choices[0].message.content.strip()
                except Exception as e:
                    plant_info = "Information not available."

            else:
                plant_image.species = "Unable to identify specie. Please Try again and ensure you upload a plant image."
                plant_info = "Information not available."

            return render(request, 'image_upload/image_result.html', {
                'plant_image': plant_image,
                'plant_info': plant_info
            })
    else:
        form = PlantImageForm()
    return render(request, 'image_upload/home.html', {'form': form})


# Created a new view function for the biodiversity page
def biodiversity(request):
    return render(request, 'image_upload/biodiversity.html')


def tutorial(request):
    return render(request, 'image_upload/tutorial.html')
