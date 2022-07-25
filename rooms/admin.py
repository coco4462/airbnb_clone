from django.contrib import admin
from . import models

@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule) 
class Itemadin(admin.ModelAdmin):

    """ Item Admin Definition """

    pass


# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Admin Definition """

    pass