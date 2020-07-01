from django.contrib import admin
from .models import ReservationTable, weeklyFeaturedFood, NewsLetter

admin.site.register(ReservationTable)
admin.site.register(weeklyFeaturedFood)
admin.site.register(NewsLetter)