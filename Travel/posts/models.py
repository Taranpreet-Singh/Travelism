from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth import settings
# Create your models here.

User = get_user_model()

class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='')
    caption = models.TextField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    upload_date = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return self.User.username

    def get_absolute_url(self):
        return reverse('posts:post_list', kwargs={'username': self.user.username})

    class Meta:
        ordering = ['-upload_date']


# class Comment(models.Model):
#     post = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE)
#     comment = models.TextField()
#     upload_date = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.comment
