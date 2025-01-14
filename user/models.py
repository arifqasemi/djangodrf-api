from django.db import models
from authemail.models import EmailUserManager, EmailAbstractUser


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
class Customer(EmailAbstractUser):
	is_admin = models.BooleanField(default=False)
	date_of_birth = models.CharField('date of birth', max_length=50, null=True, blank=True)
	is_customer = models.BooleanField(default=False)

	objects = EmailUserManager()