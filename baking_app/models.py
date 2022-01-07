from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryResource

class Bake(models.Model):
    """Bake Model

    Fields:
        recipe_url: The URL of the original recipe
        date: the date it was baked
        description: overview of the bake process
        title: name of the bake
        category: the type of recipe
    """
    recipe_url = models.URLField()
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    title = models.CharField(max_length=150)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    success = models.BooleanField(default=False)

    @property
    def hero_img(self):
        """Return the hero image for the bake

        Returns:
            string: The url of the hero image
        """
        cloudinary: CloudinaryResource = Image.objects.get(step__bake=self, is_hero=True).image
        url = cloudinary.build_url(height=480, width=640, format='jpg')
        return url

    def __str__(self):
        return self.title


class Category(models.Model):
    """Category Model

    Fields:
        label: label of the category
    """
    label = models.CharField(max_length=50)

    def __str__(self):
        return self.label


class Image(models.Model):
    """Image model

    Fields:
        step: The step it's associated with
        image: Cloudinary image
        is_hero: Should the image be featured in the bake
    """
    step = models.ForeignKey('Step', on_delete=models.CASCADE)
    image = CloudinaryField('image')
    is_hero = models.BooleanField(default=False)

    @property
    def jpg_url(self):
        """Returns the correctly formated image

        Returns:
            string: The image url as a jpg
        """
        return self.image.build_url(height=480, width=640, format='jpg')


class Step(models.Model):
    """Step Model

    Fields:
        bake: The associated bake
        text: notes for the step
        position: order of the step

    Returns:
        [type]: [description]
    """
    bake = models.ForeignKey('Bake', on_delete=models.CASCADE)
    text = models.TextField()
    position = models.IntegerField()

    def __str__(self):
        return f'{self.bake.title} step #{self.position}'
