# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:44:35 2016

@author: david
"""
from django.db import models


class DateModel(models.Model):
    """Handles creation and modification dates."""
    
    class Meta:
        abstract = True
    
    id = models.AutoField(primary_key=True)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    