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
class Event_authorized_user(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE,related_name = 'eauu')
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Performance(models.Model) :
    choice_ticket = (
    (0, 'Not available'),
    (1, 'Available')
    )

    performance_id = models.AutoField(primary_key=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='performance')
    streaming_method = models.SmallIntegerField(choices=((1,"APP"),(2,"OBS")),null = True)
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField(null=True)
    end_datetime = models.DateTimeField(null=True)
    capacity =models.IntegerField(null = True)
    ticket_available_flag = models.SmallIntegerField(choices= choice_ticket, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        if(self.event.type == 2) :
            self.streaming_method = None

        super(Performance, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Ticket(models.Model) :
    choice_draw = (
    (0, 'No drawing'),
    (1, 'By drawing')
    )
    choice_status = (
    (0, 'Drawing preiod'),
    (1, ' Purchase method')
    )
    choice_flag = (
    (0, 'Not available'),
    (1, 'Available')
    )
    choice_seat = (
    (0, 'Not assigned'),
    (1, 'Assigned')
    )
    ticket_id = models.AutoField(primary_key=True)
    performance = models.ForeignKey(Performance, on_delete= models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    points_required = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    expiration_datetime = models.DateTimeField(auto_now_add=True)
    drawing_flag = models.SmallIntegerField(choices= choice_draw, default=1)
    drawing_application_deadline = models.DateTimeField(null=True)
    drawing_status = models.SmallIntegerField(choices=choice_status, default=1)
    stamp_available_flag = models.SmallIntegerField(choices= choice_flag, default=1)
    max_number_of_ticket = models.IntegerField()
    number_of_issued_tickets = models.IntegerField()
    is_seat_id_assigned = models.SmallIntegerField(choices=choice_seat, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.drawing_flag == 0 :
            self.drawing_status = 1
        elif self.drawing_flag == 1 :
            self.drawing_status = 0

        super(Ticket, self).save(*args, **kwargs)

class Drawing(models.Model):
    choice_elect = (
    (0,'Not elected'),
    (1, 'Elected')
    )
    choice_purchase = (
    (0, 'Not purchased'),
    (1, 'Purchased')
    )
    ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='ticketmodel')
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name='user_drawing')
    is_elected = models.SmallIntegerField(choices=choice_elect, default=1)
    is_purchased = models.SmallIntegerField(choices=choice_purchase, default=1)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.username