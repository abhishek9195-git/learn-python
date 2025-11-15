from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField()
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()

    def __str(self):
        return self.comment