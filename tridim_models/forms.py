# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 23:01:29 2016

@author: david
"""
from django.forms import ModelForm
from django.contrib.auth.models import User

from tridim_models.models import RegisteredUser


class UserForm(ModelForm):

    class Meta:
        model = User  
        fields = ["username", "password"]

class RegisteredUserForm(ModelForm):
    class Meta:
        model = RegisteredUser
        fields = ['first_name', 'last_name', 'phone_number', 'email']
