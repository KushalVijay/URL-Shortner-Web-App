from django.db import models

# Create your models here.
from django_hosts.resolvers import reverse
from .validators import validate_dot_com,validate_url

from .utils import random_shortcode_generator
# class OnwayManager(models.Manager):




class Onway(models.Model):
    url = models.CharField(max_length=250,validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=15,unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    #active =  models.BooleanField(default=False)




    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = random_shortcode_generator(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(Onway, self).save(*args, **kwargs)

    def get_short_url(self):
        url_path =  "http://www.Onway.com/" + self.shortcode #reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path



