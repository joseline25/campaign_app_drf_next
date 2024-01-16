from django.db import models
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
# Create your models here.


class Campaign(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    slug = models.SlugField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    logo = CloudinaryField('Image', overwrite=True, format='.jpg')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    # create the slug depending on the title

    def save(self, *args, **kwargs):
        to_assign = slugify(self.title)
        # make the slug unique knowing that title are not unique
        # so basically if a similar slug already exists then
        # regenrate it using another function for our example
        # we are appending the number of the item in the db to the slug

        if Campaign.objects.filter(slug=to_assign).exists():
            to_assign = to_assign + str(Campaign.objects.all().count())

        # set the value of the slug field when saving
        self.slug = to_assign

        # on renvoit la main à la méthode save originale
        super().save(*args, **kwargs)


class Subscriber(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.DO_NOTHING)
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email
