# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    phoneno = models.IntegerField(null=True, blank=True)
    address = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Wallet(models.Model):

    #__Wallet_FIELDS__
    user_id = models.IntegerField(null=True, blank=True)
    amount = models.CharField(max_length=255, null=True, blank=True)
    refno = models.CharField(max_length=255, null=True, blank=True)
    status = models.BooleanField()

    #__Wallet_FIELDS__END

    class Meta:
        verbose_name        = _("Wallet")
        verbose_name_plural = _("Wallet")


class Transaction(models.Model):

    #__Transaction_FIELDS__
    wallet_id = models.IntegerField(null=True, blank=True)
    datec = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Transaction_FIELDS__END

    class Meta:
        verbose_name        = _("Transaction")
        verbose_name_plural = _("Transaction")



#__MODELS__END
