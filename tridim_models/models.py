from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from sketchfab_test.utils import DateModel


class RegisteredUser(DateModel):
    """Contains user data and links to its uploaded 3D models."""
    
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    
    
class UploadedModel(DateModel):
    """Describes a 3D model uploaded by a user."""
    
    # Automatically delete orphan 3D models
    creator = models.ForeignKey(
        RegisteredUser, on_delete=models.CASCADE, related_name="models")
        
    name = models.CharField(max_length=255)
    description = models.TextField(
        default=u"The user did not provide a description for this model.")
    nb_views = models.IntegerField(default=0)
        