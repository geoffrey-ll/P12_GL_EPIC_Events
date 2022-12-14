from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.managers import MyUserManager


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # Doit créer un validateur pour vérifier un format de numéro de téléphone.
    phone = models.PositiveBigIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    class Meta:
        abstract = True


class Employee(AbstractBaseUser, Person):

    class PossibleTeam(models.TextChoices):
        WEBMASTER = "WM", _("Webmaster")
        MANAGER = "MA", _("Manager")
        SALES = "SA", _("Sales")
        SUPPORT = "SU", _("Support")

    email = models.EmailField(max_length=255, unique=True,
                              verbose_name='email address')
    team = models.CharField(choices=PossibleTeam.choices,
                            default=PossibleTeam.SALES, max_length=2)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["team", "first_name", "last_name", "phone"]


    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin or self.is_staff

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    # class Meta:
    #     verbose_name_plural = "Users"


    def __str__(self):
        return self.email


class ManagerTeamEmployee(Employee):
    """Modèle pour les employés de l'équipe de management."""
    pass


class SalesTeamEmployee(Employee):
    """Modèle pour les employés de l'équipe de ventes."""
    pass


class SupportTeamEmployee(Employee):
    """Modèle poure les employés de l'équipe de support."""
    pass
