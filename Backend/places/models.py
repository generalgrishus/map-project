import uuid
from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True) 
    lon = models.DecimalField("longitude", max_digits=9, decimal_places=6)
    lat = models.DecimalField("latitude", max_digits=9, decimal_places=6)
    description = models.TextField(blank=True, null=True)
    #image =
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_visited = models.BooleanField(default=False)