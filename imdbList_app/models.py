from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=200)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE , related_name='watchlists')
    active = models.BooleanField(default=True) # launched or not
    avg_rating = models.FloatField(default=0)
    number_rating = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True) # when the watchlist was created
     
    
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    review_user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description= models.CharField(max_length=100 , null = True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.rating) + " | " +  self.watchlist.title + " | " + self.review_user.username