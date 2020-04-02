from django.db import models

# Create your models here.

# Very simple model of a post.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models. TextField()         # This will become a one to many relationship once we have a users table

    def __str__(self):
        return self.title + 'by: ' + 'author'