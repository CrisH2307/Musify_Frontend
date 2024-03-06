"""
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=255)  
    artist_id = models.SlugField(unique=True, max_length=255)
    image = models.ImageField(upload_to='artist_images/', blank=True, null=True) 

    def __str__(self): 
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255, default='Untitled Album')
    release_date = models.DateField(null=True, blank=True)
    album_id = models.CharField(max_length=255, unique=True) 
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):  
        return self.title
    

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.DurationField(null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "song"
        ordering = ['created_on']

    def __str__(self):
        return self.title
"""