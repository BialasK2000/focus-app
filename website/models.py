from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Task(models.Model):
    name = models.CharField(max_length=69)
    description = models.TextField(max_length=1337)
    deadline = models.DateField()
    status = models.BooleanField("I am currently doing this")
    visible = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-status', 'deadline']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(default='default.jpg', upload_to='profile_images', blank=True, null=True)
    bio = models.TextField(default='Write Your bio here...')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)
