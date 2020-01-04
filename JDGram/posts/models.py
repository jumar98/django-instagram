from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    """Post model"""

    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    def __str__(self):
        """Return the title and username"""
        return "Posted {} by @{}".format(self.title, self.user.username)