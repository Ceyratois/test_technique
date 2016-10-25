from django.test import TestCase
from django.contrib.auth.models import User

from tridim_models.models import RegisteredUser, UploadedModel
from badges.models import Badge, BadgeType

class BadgesTest(TestCase):
    
    def setUp(self):
        
        self.dj_user = User()
        self.dj_user.save()
        
        self.user = RegisteredUser(user=self.dj_user, first_name="John", last_name="Doe")
        self.user.save()
    
    def test_badge_associated_to_user(self):
        badge_type = BadgeType.objects.get(identifier="models_1")
        badge = Badge(proprietary=self.user, badge_type=badge_type)
        badge.save()
        
        self.assertEqual(1, self.user.badges.count())
        self.assertEqual(badge, self.user.badges.all()[0])
        
    def test_award_1model(self):
        
        model = UploadedModel(creator=self.user, nb_views=0)
        model.save()
        
        self.assertEqual(1, self.user.badges.count())
        
        badge = self.user.badges.first()
        
        self.assertEqual(badge.badge_type.identifier, "models_1")
        
    def test_award_5model(self):
        
        for i in range(5):
            model = UploadedModel(creator=self.user, nb_views=0)
            model.save()
        
        self.assertEqual(2, self.user.badges.count())
        
        badge_identifiers = [badge.badge_type.identifier for badge in self.user.badges.all()]
        
        self.assertEqual(badge_identifiers, ["models_1", "models_5"])
        
    def test_award_10model(self):
        
        for i in range(10):
            model = UploadedModel(creator=self.user, nb_views=0)
            model.save()
        
        self.assertEqual(3, self.user.badges.count())
        
        badge_identifiers = [badge.badge_type.identifier for badge in self.user.badges.all()]
        
        self.assertEqual(badge_identifiers, ["models_1", "models_5", "models_10"])
