# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:32:58 2016

@author: david
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from tridim_models.models import UploadedModel
from badges.models import Badge, BadgeType

badge_types_to_create = {
    "views_10": "local",
    "views_1000": "local",
    "views_1000000": "local",
    "models_1": "global",
    "models_5": "global",
    "models_10": "global"
}

def award_badge(badge_identifier, user, model=None):
    """Create badge object related to user and model."""
    
    
    badge_type = BadgeType.objects.get(identifier=badge_identifier)
    badge = Badge(badge_type=badge_type, proprietary=user, model=model)
    try:
        badge.save()
    except Badge.AlreadyExists:
        pass


# Badges for views number
@receiver(post_save, sender=UploadedModel, dispatch_uid="badge_views_number")
def award_badges_for_views_number(sender, instance, **kwargs):
    
    if instance.nb_views >= 1000000:
        award_badge("views_1000000", user=instance.creator, model=instance)
    if instance.nb_views >= 1000:
        award_badge("views_1000", user=instance.creator, model=instance)
    if instance.nb_views >= 10:
        award_badge("views_10", user=instance.creator, model=instance)
      

# Badges for created models number
@receiver(post_save, sender=UploadedModel, dispatch_uid="models_created_number")
def award_badges_for_models_number(sender, instance, **kwargs):

    if instance.creator.models.count() > 0:    
        award_badge("models_1", user=instance.creator)
        
    if instance.creator.models.count() > 4:    
        award_badge("models_5", user=instance.creator)
        
    if instance.creator.models.count() > 9:    
        award_badge("models_10", user=instance.creator)
