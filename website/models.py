from django.db import models

# Create your models here.
# Contact Hero Section
class ContactHero(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='contact/hero/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


    @property
    def progress_percent(self):
        try:
            if self.goal_amount and self.goal_amount > 0:
                return int((self.raised_amount / self.goal_amount) * 100)
        except:
            pass
        return 0
    


# Contact Information
class ContactInfo(models.Model):
    address = models.TextField()
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True)
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True)
    working_hours = models.TextField()

    def __str__(self):
        return "Contact Information"


# Google Map
class ContactMap(models.Model):
    map_embed_url = models.TextField()

    def __str__(self):
        return "Google Map"


# Contact Team
class ContactTeam(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(upload_to='contact/team/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Donation(models.Model):
    name= models.CharField(max_length=200)
    phone   = models.CharField(max_length=15, blank=True, null=True)
    email= models.EmailField()
    cardno = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    cause = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True) 


class DonationMessage(models.Model):
    SUBJECT_CHOICES = [
        ("donation", "Donation Inquiry"),
        ("volunteer", "Volunteer"),
        ("partnership", "Partnership"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.CharField(max_length=20, choices=SUBJECT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    

from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name