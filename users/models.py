from django.db import models

from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


# Create your models here.
class Clients(models.Model):
    choice_archive = (
        (0, 'Not archived'),
        (1, 'Archived')
    )
    client_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    seconds_delivered_per_month = models.DecimalField(max_digits=15, decimal_places=0, null=False)
    is_archived = models.SmallIntegerField(null=False, choices=choice_archive, default=1)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)

    def __str__(self):
        return self.name

class Prefectures(models.Model):
    choice_default = (
        (0 , 'Not default'),
        (1 , 'Default') )
    prefecture_id = models.IntegerField(primary_key=True, null=False)
    name = models.CharField(max_length=45, null=False)
    display_order = models.SmallIntegerField(null=False)
    is_default = models.SmallIntegerField(null=False, choices=choice_default)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)

    def __str__(self):
        return self.name

class Users(models.Model):
    choice_user = (
        (1, 'General user'),
        (2, 'Host user')
    )
    choice_login = (
        ('email', 'EMAIL'),
        ('insta', 'INSTAGRAM'),
        ('facebook', 'FACEBOOK'),
        ('twitter', 'TWITTER')
    )
    choice_sex = (
        (0, 'Not known'),
        (1, 'Male'),
        (2, 'Female'),
        (9, 'Not applicable')
    )
    choice_sex_public = (
        (0, 'Private'),
        (1, 'Public')
    )
    choice_user_type = (
        (1, 'Individual'),
        (2, 'Group')
    )
    choice_auth = (
        (0, 'Not authenticated'),
        (1, 'Authenticated'),
        (2, 'No authenticated required')
    )
    choice_archive = (
        (0, 'Not archived'),
        (1, 'Archived')
    )
    user_id = models.IntegerField(primary_key=True, null=False)
    client_id = models.ForeignKey(Clients, on_delete=models.CASCADE)
    user_type = models.SmallIntegerField(null=False, default=0,choices=choice_user )
    login_type = models.CharField(max_length=45, null=False, default='email', choices=choice_login)
    email = models.CharField(max_length=254, null=True)
    password = models.CharField(max_length=255, null=True)
    remember_token = models.CharField(max_length=255, null=True)
    facebook_id = models.CharField(max_length=255, null=True)
    twitter_id = models.CharField(max_length=255, null=True)
    apple_id = models.CharField(max_length=255, null=True)
    last_name_kanji = models.CharField(max_length=255, null=False)
    first_name_kanji = models.CharField(max_length=255, null=False)
    last_name_kana = models.CharField(max_length=255, null=False)
    first_name_kana = models.CharField(max_length=255, null=False)
    nickname = models.CharField(max_length=255, null=False)
    sex = models.SmallIntegerField(null=False, choices=choice_sex, default=1)
    is_sex_public = models.SmallIntegerField(null=False, choices=choice_sex_public, default=1)
    date_of_birth = models.DateField(null=False)
    is_date_of_birth_public = models.SmallIntegerField(null=False, choices=choice_sex_public, default=1)
    phone = models.CharField(max_length=45, null=True)
    zip_code = models.CharField(max_length=8, null=True)
    prefecture_id = models.ForeignKey(Prefectures, max_length=11, on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=255, null=True)
    subsequent_address = models.CharField(max_length=255, null=True)
    biography = models.TextField(null=True)
    points_balance = models.DecimalField(max_digits=15, decimal_places=0, null=False)
    points_reveived = models.DecimalField(max_digits=15, decimal_places=0, null=False)
    stamps_balance = models.DecimalField(max_digits=15, decimal_places=0, null=False)
    econtext_cus_id = models.CharField(max_length=255, null=True)
    delux_membership = models.CharField(max_length=255, null=True)
    host_user_type = models.SmallIntegerField(null=True, choices=choice_user_type, default=1)
    is_authenticated = models.SmallIntegerField(null=False, default=1, choices=choice_auth)
    is_archived = models.SmallIntegerField(null=False, default=1, choices=choice_archive)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)

    # def __str__(self):
    #     return self.nickname
    def __str__(self):
        return self.email

