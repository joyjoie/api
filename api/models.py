from django.db import models
import datetime as dt

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to="image/")
    Details = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
