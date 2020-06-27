from django.db import models

class ReservationTable(models.Model):

        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=50)
        phoneNumber =  models.IntegerField()
        time = models.CharField(max_length=20)
        day = models.CharField(max_length=20)
        no_persons = models.IntegerField()

        def __str__(self):
                return self.name + ' '  + str(self.time) + str(self.no_persons)