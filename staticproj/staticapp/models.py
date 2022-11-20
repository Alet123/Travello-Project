from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

class People(models.Model):
    nam1 = models.CharField(max_length=250)
    img1 = models.ImageField(upload_to='pics')
    des1 = models.TextField()

    def __str__(self):
        return self.name

