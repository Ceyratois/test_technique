# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:44:35 2016

@author: david
"""
from tridim_models.models import RegisteredUser, UploadedModel
from badges.models import Badge
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RegisteredUser
        fields = ('first_name', 'last_name', 'email', 'phone_number')


class BadgeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Badge
        fields = ('url', 'category', 'description', 'proprietary')


class TridimModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UploadedModel
        fields = ('name', 'description', 'nb_views')