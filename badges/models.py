from __future__ import unicode_literals

from django.db import models

from sketchfab_test.utils import DateModel


class BadgeType(models.Model):
    """Badge category."""

    id = models.AutoField(primary_key=True)

    identifier = models.CharField(max_length=255, unique=True)

    #: Local : related to a specific model (e.g. more than 1000 views)
    # Global : related to the user it self (e.g. at least 5 uploaded models)
    category = models.CharField(
        max_length=255,
        choices=[
            ("local", "local"),
            ("global", "global")
        ]
    )

    description = models.TextField(default="Description missing.")


class Badge(DateModel):
    """Represents awards (achievements) given to users meeting specific conditions."""

    proprietary = models.ForeignKey(
        "tridim_models.RegisteredUser", on_delete=models.CASCADE, related_name="badges")

    model = models.ForeignKey(
        "tridim_models.UploadedModel",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="badges"
    )

    badge_type = models.ForeignKey("BadgeType", on_delete=models.CASCADE, related_name="badges")

    @property
    def category(self):
        return self.badge_type.category

    @property
    def description(self):
        return self.badge_type.description

    class Meta:
        unique_together = ('badge_type', 'proprietary', 'model')

    class AlreadyExists(Exception):
        """Raised when trying to create a badge when a similar one already exists."""

    def save(self, *args, **kwargs):
        """Validate category - model couple before saving the object."""

        if self.category == "local" and self.model is None:
            raise ValueError("A local badge must have a related model !")

        if self.category == "global" and self.model is not None:
            raise ValueError("A global badge can not have a related model !")

        # Do not create a badge of the same class than an already existing one
        if self.category == "global" and self.id is None:
            if Badge.objects.filter(
                proprietary=self.proprietary, badge_type__identifier=self.badge_type.identifier
            ).count():
                raise self.AlreadyExists("A badge of the same type already exists for this user.")

        super(Badge, self).save(*args, **kwargs)
