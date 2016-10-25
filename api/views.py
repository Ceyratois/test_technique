# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 20:32:58 2016

@author: david
"""

from tridim_models.models import RegisteredUser, UploadedModel
from badges.models import Badge
from rest_framework import viewsets
from api.serializers import UserSerializer, BadgeSerializer, TridimModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""

    queryset = RegisteredUser.objects.all().order_by('-created_at')
    serializer_class = UserSerializer


class TridimModelViewSet(viewsets.ModelViewSet):
    """API endpoint that allows 3D models to be viewed."""

    queryset = UploadedModel.objects.all()
    serializer_class = TridimModelSerializer


class BadgeViewSet(viewsets.ModelViewSet):
    """API endpoint that allows badges to be viewed."""

    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer