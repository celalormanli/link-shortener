from django.db import models
from rest_framework_api_key.models import APIKey

class Link(models.Model):
    main_link = models.URLField(max_length=250) 
    shorted_link=models.CharField(max_length=10, unique=True)
    redirect_counter=models.PositiveIntegerField(default=0)
    api_key=models.ForeignKey(APIKey, on_delete=models.CASCADE)