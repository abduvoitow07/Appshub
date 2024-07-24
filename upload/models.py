from django.db import models


class Application(models.Model):
    app = models.CharField(max_length=100)
    version = models.CharField(max_length=100)
    size = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='logo/')
    file = models.FileField(upload_to='file/')

    def __str__(self):
        return self.app
