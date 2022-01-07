from tkinter import Image
from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryResource

class Bake(models.Model):
    recipe_url = models.URLField()
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    title = models.CharField(max_length=150)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    success = models.BooleanField(default=False)

    @property
    def images(self):
        return Images.objects.filter(step__bake=self)

    @property
    def hero_img(self):
        cloudinary: CloudinaryResource = self.images.get(is_hero=True).image
        url = cloudinary.build_url(height=480, width=640, format='jpg')
        return url

    def __str__(self):
        return self.title


class Category(models.Model):
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Images(models.Model):
    step = models.ForeignKey('Step', on_delete=models.CASCADE)
    image = CloudinaryField('image')
    is_hero = models.BooleanField(default=False)

    @property
    def jpg_url(self):
        return self.image.build_url(height=480, width=640, format='jpg')


class Step(models.Model):
    bake = models.ForeignKey('Bake', on_delete=models.CASCADE)
    text = models.TextField()
    position = models.IntegerField()

    def __str__(self):
        return f'{self.bake.title} step #{self.position}'
