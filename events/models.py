
from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Existing image URL support
    image = models.URLField(blank=True)

    # Upload image directly from computer
    image_file = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
