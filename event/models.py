from django.db import models
# from user.models import Clients
# Create your models here.
class Event(models.Model) :
    choice_type = (
    (1 , 'Live stream event'),
    (2 , 'Office event'))
    choice_private = (
    (0 , 'Not private'),
    (1 , 'Private') )
    choice_archive = (
    (0 , 'Not archived'),
    (1 , 'Archived'))
    event_id = models.AutoField(primary_key=True)
    client = models.ForeignKey("user.Client", on_delete=models.CASCADE)
    type = models.IntegerField(choices = choice_type)
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_private = models.IntegerField(choices = choice_private, default =1)
    private_key = models.CharField(max_length=255, null=True)
    is_archived = models.IntegerField(choices = choice_archive)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title
