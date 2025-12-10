from django.db import models

class About(models.Model):
  about_heading = models.CharField(max_length=25)
  about_body = models.TextField(max_length=250)

  def __str__(self):
    return self.about_heading
  
class Links(models.Model):
  social_media = models.CharField(max_length=20)
  link = models.URLField()

  def __str__(self):
    return self.social_media