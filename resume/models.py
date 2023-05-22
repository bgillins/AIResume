from django.db import models
import uuid

class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    career_interest = models.CharField(max_length=200, null=True, blank=True)  # new field
