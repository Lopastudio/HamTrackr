from django.db import models

class Contact(models.Model):
    callsign = models.CharField(max_length=20)
    frequency = models.FloatField()
    mode = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.callsign} - {self.date_time}"
