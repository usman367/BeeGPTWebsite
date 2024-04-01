from django.db import models


# Model to store the plant image and species name
class PlantImage(models.Model):
    image = models.ImageField(upload_to='plant_images/')  # Saves the image in the media/plant_images directory
    species = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.species or "Unknown"

