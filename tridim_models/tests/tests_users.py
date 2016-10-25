from django.test import TestCase
from django.contrib.auth.models import User

from tridim_models.models import RegisteredUser, UploadedModel


class UserTests(TestCase):
    """Tests about user registration."""
    
    def test_user_creation(self):
        
        dj_user = User()
        dj_user.save()
        
        user = RegisteredUser(user=dj_user, first_name="John", last_name="Doe")
        user.save()
