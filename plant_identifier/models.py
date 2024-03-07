from django.db import models


# Create your models here.
class PlantImage(models.Model):
    image = models.ImageField(upload_to='plant_images/')
    species = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.species or "Unknown"

