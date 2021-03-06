from email.policy import default
from statistics import mode
from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    song_title = models.CharField(max_length=200)
    featured_image =models.ImageField(null=True,blank=True, default='default.jpg')
    release_date =  models.DateTimeField(null=True,blank=True)
    author=models.ForeignKey('Author',related_name='unit_song',on_delete=models.SET_NULL,null=True,blank=True)    
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
  
    def __str__(self):        
        return self.song_title
    @property
    def imageUrl(self):        
        try:
            img= self.featured_image.url
        except:
            img= ""
        return img
        
class Author(models.Model):
    author_name = models.CharField(max_length=200)
    author_surname = models.CharField(max_length=200)
    # featured_image =models.ImageField(null=True, blank=True, default='default.jpg')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
       return f'{self.author_name} {self.author_surname}'
    
class PlaylistSong(models.Model):  
    list_title = models.CharField(max_length=200)  
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    songs= models.ManyToManyField(Song)    
    
    def __str__(self):
      return self.list_title