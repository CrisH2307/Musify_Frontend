from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    artistid = models.AutoField(primary_key=True)
    artistimg = models.TextField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)

    def str(self):  
        return self.name

class Album(models.Model):
    artistid = models.ForeignKey(Artist, on_delete=models.CASCADE)
    albumid = models.AutoField(primary_key=True)
    albumtitle = models.CharField(max_length=255)
    albumimg = models.TextField(blank=True, null=True)
    date = models.IntegerField(blank=True, null=True)

    def str(self):  
        return self.title

class Song(models.Model):
    albumid = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    songid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    duration = models.IntegerField(blank=True, null=True)

    def str(self):  
        return self.title