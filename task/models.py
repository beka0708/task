from django.db import models


class Task(models.Model):
    # id_task = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
