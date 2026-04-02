from django.db import models

class tasks(models.Model):
    title = models.CharField(max_length=100)
    due_date = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Reminder(models.Model):
    task = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.task


class feedback(models.Model):
    mood = models.CharField(max_length=50)
    note = models.TextField()

    def __str__(self):
        return self.mood