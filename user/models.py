from django.db import models
from event.models import Event
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Client(models.Model):
    choice_archive = (
        (0, 'Not archived'),
        (1, 'Archived')
    )
    client_id = models.AutoField(primary_key=True)
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

class User(AbstractUser):
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
    user_id = models.AutoField(primary_key=True, null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True,null=True)
    user_type = models.SmallIntegerField(null=False, default=0,choices=choice_user)
    login_type = models.CharField(max_length=45, null=False, default='email', choices=choice_login)
    sex = models.SmallIntegerField(null=False, choices=choice_sex, default=1)
    is_sex_public = models.SmallIntegerField(null=False, choices=choice_sex_public, default=1)
    date_of_birth = models.DateField(null=True,blank=True)
    is_date_of_birth_public = models.SmallIntegerField(null=False, choices=choice_sex_public, default=1)
    phone = models.CharField(max_length=45, null=True , blank=True)
    zip_code = models.CharField(max_length=8, null=True,blank=True)
    prefecture_id = models.ForeignKey(Prefectures, max_length=11, on_delete=models.SET_NULL, null=True,blank=True)
    biography = models.TextField(null=True,blank=True)
    points_balance = models.DecimalField(max_digits=15, decimal_places=0, null=True,blank=True)
    host_user_type = models.SmallIntegerField(null=True, choices=choice_user_type, default=1)
    isAuthenticated = models.SmallIntegerField(null=True, default=1, choices=choice_auth)
    is_archived = models.SmallIntegerField(null= True, default=1, choices=choice_archive)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    updated_at = models.DateTimeField(null=False, auto_now=True)
    avatar = models.CharField(max_length=255,null=True,blank= True)

    # def __str__(self):
    #     return self.username

class Address(models.Model):
    recipient_phone = models.CharField(max_length=15, null=False,blank=False)
    address_detail = models.TextField(default='',null=False,blank=False)
    recipient_name = models.CharField(max_length=50,default=None)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE,null=False,blank=False)

class Box_notification_trans_content(models.Model):
    choice_type = (
        (1, 'Host user'),
        (2, 'Client user (Mgmt portal user)'),
        (3, 'System admin user( Mgmt portal user)'))
    choice_deliver = (
        (0, 'Not delivered'),
        (1, 'Delivered'))
    box_notification_trans_content_id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    from_type = models.IntegerField(choices=choice_type, default=1)
    from_user_id = models.IntegerField(null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    to_user_ids = models.TextField(null=True)
    scheduled_at = models.DateTimeField(auto_now_add=True)
    is_delivered = models.IntegerField(choices=choice_deliver)
    delivered_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Image_paths(models.Model):
    user = models.ForeignKey(User, on_delete = models.SET_NULL,null=True,blank=True)
    event = models.ForeignKey(Event, on_delete = models.SET_NULL,null=True,blank=True,related_name='event_img')
    box_notification_trans_content_id = models.ForeignKey(Box_notification_trans_content, on_delete = models.SET_NULL,null=True,blank=True)
    file_name = models.CharField(max_length=255, null=False)
    dir_path = models.CharField(max_length=255, null=False)
    image_url = models.CharField(max_length=255,null=True,blank=True)
    display_order = models.SmallIntegerField(null=False)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)

    # def __str__(self):
    #     return self.file_name

    def save(self, *args, **kwargs):
        self.image_url = self.dir_path+self.file_name
        super(Image_paths, self).save(*args, **kwargs)
