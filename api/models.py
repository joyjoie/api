from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=60)
    image = models.ImageField(upload_to="image/")
    details = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    @classmethod
    def display_images(cls):
        return cls.objects.all()

    @classmethod
    def index(cls):
        today = dt.date.today()
        yo = cls.objects.filter(pub_date__date=today)
        return yo



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=60 ,blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
       self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, bio):
        self.bio = bio
        self.save()

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile

    @classmethod
    def pro(cls):
        return cls.objects.all()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Comments(models.Model):
    img = models.ForeignKey(Image)
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=60)

    @classmethod
    def display_comments(cls):
        return cls.objects.all()

    def save_comments(self):
        self.save()


