from django.db import models

# Create your models here.

class Log(models.Model):
    title = models.CharField(max_length = 180)
    timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    completed = models.BooleanField(default = False, blank = True)
    updated = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return self.title
class Wallet(models.Model):
    class TransactionType(models.TextChoices):
        REFOUND = 'Refound', '12'
        TRANSFER = 'Transfer', '13'
        ORDER = 'Order', '14'
        DEDUCTION = 'Deduction', '15'

    total   = models.IntegerField(blank = False)
    amount    = models.IntegerField(blank = False, default = 0)
    user_id = models.BigIntegerField(blank = False)
    transactiontype = models.CharField(max_length=20,blank = False,
    choices=TransactionType.choices, default=TransactionType.TRANSFER)
    transactiondate = models.DateTimeField(blank = False)
    reference_id = models.CharField(max_length = 15)
