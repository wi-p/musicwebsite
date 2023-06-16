from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Singer(models.Model):
    name = models.CharField(max_length = 100)
    photo = models.FileField(upload_to = 'images/website/singers/')
    slug = models.SlugField(unique = True, blank = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Singer, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
        
        
class PlayList(models.Model):
    name = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    gender = models.CharField(max_length = 50)
    ply_number = models.IntegerField(default = 0)
    dwnld_number = models.IntegerField(default = 0)
    slug = models.SlugField(unique = False, blank = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PlayList, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
        
        
class Music(models.Model):
    name = models.CharField(max_length = 100)
    gender = models.CharField(max_length = 100)
    ply_number = models.IntegerField(default = 0)
    pub_date = models.DateTimeField()
    dwnld_number = models.IntegerField(default = 0)
    singer = models.ForeignKey(Singer, on_delete = models.CASCADE)
    file = models.FileField(upload_to = 'musics/')
    playlist = models.ManyToManyField(PlayList)
    slug = models.SlugField(unique = False, blank = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Music, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
        
        
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField()
    rgst_date = models.DateTimeField()
    password = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.name