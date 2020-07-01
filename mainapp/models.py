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

class weeklyFeaturedFood(models.Model):
        id = models.AutoField(primary_key=True)
        title = models.CharField(max_length=200)
        detail = models.CharField(max_length=500)
        foodImage = models.ImageField(upload_to='weeklyFeatured', null=True, blank=True)
        price = models.IntegerField()
        slug = models.CharField(max_length=200)
        foodHour = models.CharField(max_length=30)

        def __str__(self):
                return self.title + ' ' + str(self.price)

class NewsLetter(models.Model):
        email = models.EmailField()

        def __str__(self):
                return self.email