from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone



def default_image():
    # Specify the default image URL or path here
    return 'media'


class Article(models.Model):
    GENRE_CHOICES = [
        ('Current Tech', 'Current Tech'),
        ('Tech-how-to', 'Tech-how-to'),
        ('Gaming', 'Gaming'),
        ('Review', 'Review'),
        ('Tech-Fun', 'Tech-Fun'),
        # Add more genre options as desired
    ]


    title = models.CharField(max_length=200)
    paragraph = models.TextField()
    video = models.FileField(upload_to='videos/')
    image = models.ImageField(upload_to='images/', default=default_image)
    genre = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
