from django.db import models


NEWSLETTER_OPTION = [
    ('W', 'Weekly'),
    ('M', 'Monthly')
]



# Create your models here.
class Subscribe(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    option = models.CharField(max_length=2, choices=NEWSLETTER_OPTION, default='W')
