from django.db import models

class MyModel(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    # otros campos si es necesario

    def __str__(self):
        return self.title