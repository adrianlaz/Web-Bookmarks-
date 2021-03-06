from django.db import models

# Create your models here.


class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='bookmarks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

