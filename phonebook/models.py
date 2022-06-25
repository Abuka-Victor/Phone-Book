from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.phone_number
