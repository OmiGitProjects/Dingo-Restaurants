from django.db import models

class ContactsModel(models.Model):
        name = models.CharField(max_length=50)
        email = models.EmailField()
        phone = models.IntegerField()
        message = models.TextField(max_length=5000)

        def __str__(self):
                return self.name + ' ' + self.email