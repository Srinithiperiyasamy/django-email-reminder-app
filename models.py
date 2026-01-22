from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    email = models.EmailField()
    remind_date = models.DateField()
    remind_time = models.TimeField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.title
