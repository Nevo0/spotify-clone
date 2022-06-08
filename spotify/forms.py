from django.db.models.base import Model
from django.forms import ModelForm, widgets
from django import forms
from .models import PlaylistSong


class PlaylistSongForm(ModelForm):
    
    class Meta:
        model = PlaylistSong
        fields = '__all__'  
        exclude = ('user',"songs",)
