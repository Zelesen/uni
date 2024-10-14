from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=300)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    



class Campaign(models.Model):
    STATUS_CHOICES = [
        ('created', 'Created'),
        ('running', 'Running'),
        ('closed', 'Closed'),
    ]

    campaign_name = models.CharField(max_length=255)
    audience = models.CharField(max_length=255)
    campaign_type = models.CharField(max_length=50)
    campaign_goal = models.CharField(max_length=50)
    advertisement_type = models.CharField(max_length=50)
    advertisement_text = models.TextField()
    ad_file = models.FileField(upload_to='ads/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='created')

    def __str__(self):
        return self.campaign_name



class Audience(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    interest = models.CharField(max_length=255)

    def __str__(self):
        return self.name
