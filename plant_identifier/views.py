import os
from django.conf import settings
from django.shortcuts import render
from openai import OpenAI
from .forms import PlantImageForm
import requests
from keras.models import load_model
from keras.preprocessing import image
import numpy as np


# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = PlantImageForm(request.POST, request.FILES)
        if form.is_valid():
            plant_image = form.save()

            # Call to PlanetNet API
            planet_net_species, prediction_status = identify_species_using_planet_net(plant_image)
            if prediction_status:
                predicted_class = identify_species_using_local_model(plant_image)

            plant_info = fetch_plant_info(planet_net_species) if prediction_status else "Information not available."

            return render(request, 'image_upload/image_result.html', {
                'plant_image': plant_image,
                'plant_info': plant_info,
                'predicted_class': predicted_class if prediction_status else "Identification failed"
            })
    else:
        form = PlantImageForm()
    return render(request, 'image_upload/home.html', {'form': form})


# Created a new view function for the biodiversity page
def biodiversity(request):
    return render(request, 'image_upload/biodiversity.html')


def tutorial(request):
    return render(request, 'image_upload/tutorial.html')


def identify_species_using_planet_net(plant_image):
    api_url = 'https://my-api.plantnet.org/v2/identify/all'
    api_key = '2b10kJ93KxHKQXXnSGKDxuRpfe'
    files = {'images': plant_image.image}
    response = requests.post(api_url, files=files, headers={'Authorization': f'Bearer {api_key}'})

    if response.status_code == 200:
        data = response.json()
        common_name = data["results"][0]["species"]["commonNames"][0]
        plant_image.species = common_name
        plant_image.save()
        return common_name, True
    else:
        plant_image.species = "Unable to identify species. Please try again and ensure you upload a plant image."
        plant_image.save()
        return None, False


def identify_species_using_local_model(plant_image):
    model_path = os.path.join(settings.BASE_DIR, 'plant_identifier', 'models', '40EpochsTest7.keras')
    model = load_model(model_path)
    img_path = os.path.join(settings.MEDIA_ROOT, plant_image.image.name)
    processed_image = preprocess_image(img_path)
    prediction = model.predict(processed_image)
    predicted_label = np.argmax(prediction, axis=1)
    label_to_index = {
        'Bluebell': 0, 'Buttercup': 1, 'Coltsfoot': 2, 'Cowslip': 3, 'Crocus': 4,
        'Daffodil': 5, 'Daisy': 6, 'Dandelion': 7, 'Fritillary': 8, 'Iris': 9,
        'Lily Valley': 10, 'Pansy': 11, 'Snowdrop': 12, 'Sunflower': 13,
        'Tigerlily': 14, 'Tulip': 15, 'Windflower': 16
    }
    class_labels = list(label_to_index.keys())
    predicted_class = class_labels[predicted_label[0]]
    return predicted_class


def preprocess_image(img_path, target_size=(128, 128)):
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return img_array_expanded_dims


def fetch_plant_info(species):
    prompt = f"Provide biodiversity information and the animals, birds, and microorganisms {species} attracts"
    try:
        client = OpenAI(
            api_key="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"
        )
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return "Information not available."