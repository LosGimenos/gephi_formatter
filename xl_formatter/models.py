from django.db import models

class TwitterData(models.Model):
    author = models.CharField(blank=True, null=True, max_length=140)
    url = models.TextField(blank=True, null=True)
    type = models.CharField(blank=True, null=True, max_length=200)
    date = models.CharField(blank=True, null=True, max_length=100)
    author_gender = models.CharField(blank=True, null=True, max_length=100)
    city = models.CharField(blank=True, null=True, max_length=500)
    sentiment = models.CharField(blank=True, null=True, max_length=300)
    emotion = models.CharField(blank=True, null=True, max_length=300)
    author_clout = models.IntegerField(blank=True, null=True, default=None)
    contents = models.TextField(blank=True, null=True)
    media_url_http = models.TextField(blank=True, null=True)
    media_url_https = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True, default=None)
    longitude = models.FloatField(blank=True, null=True, default=None)
    followers = models.IntegerField(blank=True, null=True, default=None)
    statuses = models.IntegerField(blank=True, null=True, default=None)
    brand_source = models.CharField(blank=True, null=True, max_length=140)

class TwitterMention(models.Model):
    author = models.CharField(blank=True, null=True, max_length=140)
    mention = models.CharField(blank=True, null=True, max_length=200)
    is_Direct = models.BooleanField(default=False)
    is_Mixed = models.BooleanField(default=False)
    twitter_data = models.ForeignKey(TwitterData, on_delete=models.CASCADE, null=True)

class InstagramData(models.Model):
    author = models.CharField(blank=True, null=True, max_length=140)
    url = models.TextField(blank=True, null=True)
    type = models.CharField(blank=True, null=True, max_length=200)
    date = models.CharField(blank=True, null=True, max_length=100)
    author_gender = models.CharField(blank=True, null=True, max_length=100)
    city = models.CharField(blank=True, null=True, max_length=500)
    sentiment = models.CharField(blank=True, null=True, max_length=300)
    emotion = models.CharField(blank=True, null=True, max_length=300)
    author_clout = models.IntegerField(blank=True, null=True, default=None)
    contents = models.TextField(blank=True, null=True)
    media_url_http = models.TextField(blank=True, null=True)
    media_url_https = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True, default=None)
    longitude = models.FloatField(blank=True, null=True, default=None)
    followers = models.IntegerField(blank=True, null=True, default=None)
    statuses = models.IntegerField(blank=True, null=True, default=None)
    brand_source = models.CharField(blank=True, null=True, max_length=140)

class InstagramMention(models.Model):
    author = models.CharField(blank=True, null=True, max_length=140)
    mention = models.CharField(blank=True, null=True, max_length=200)
    is_Direct = models.BooleanField(default=False)
    is_Mixed = models.BooleanField(default=False)
    instagram_data = models.ForeignKey(InstagramData, on_delete=models.CASCADE, null=True)


