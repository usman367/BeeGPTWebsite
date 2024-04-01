from django import forms
from .models import PlantImage


# Form created to populate the 'image' field of the model
class PlantImageForm(forms.ModelForm):
    class Meta:
        model = PlantImage
        fields = ['image']
