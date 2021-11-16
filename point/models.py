from django.db import models

class User_point(models.Model) :
    choice_type = (
    (1 , 'Deposit'),
    (2 , 'Withdrawal'))
    choice_withdrawal = (
    (1 , 'Exchange for a gift'),
    (2 , 'Exchange for a ticket'))
    choice_deposit = (
    (1 , 'Purchase'),)
    user_point_id = models.AutoField(primary_key=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    type = models.IntegerField(choices=choice_type, default = 1)
    deposit_reason = models.IntegerField(null = True, choices=choice_deposit)
    withdrawal_reason = models.IntegerField(null = True, choices=choice_withdrawal)
    points = models.DecimalField(max_digits=15, decimal_places=0)
    transacted_at = models.DateTimeField(auto_now_add=True)
    points_balance = models.DecimalField(max_digits=15, decimal_places=0)
    created_at = models.DateTimeField(null=False, auto_now_add = True)
    updated_at = models.DateTimeField(null=False, auto_now = True)

    def __str__(self):
        return self.user.username