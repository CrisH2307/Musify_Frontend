from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Artist(models.Model):
    name = models.CharField(max_length=255)  
    artist_id = models.SlugField(unique=True, max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='artist_images/', blank=True, null=True) 

    def get_absolute_url(self):
        return reverse('artist_detail', args=[self.artist_id])  
    
    def save(self, *args, **kwargs):
        if not self.artist_id:
            self.artist_id = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    class Meta:
        db_table = 'artist'
        ordering = ['created_on']

    def __str__(self): 
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=255, default='Untitled Album')
    release_date = models.DateField(null=True, blank=True)

    def get_default_artist():
        default_artist = Artist.objects.first()
        return default_artist.id if default_artist else None

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums', default=get_default_artist)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "album"
        ordering = ['-release_date']  

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

