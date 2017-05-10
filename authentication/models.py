from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail


class AccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('User must have a valid email address.')
        if not kwargs.get('username'):
            raise ValueError('User must have a valid username.')


        account = self.model(
            email=self.normalize_email(email), username=kwargs.get('username')
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, password, **kwargs):

        account = self.create_user(email, password, **kwargs)
        account.is_superuser = True
        account.is_staff = True
        account.save()

        return account


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=40, unique=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    university_id = models.CharField(max_length=140, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into'
                                               'this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether the user should be'
                                                'treated as active. Unselect this instead of deleting accounts.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.email

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name]).strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)