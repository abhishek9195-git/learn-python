from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_id = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    