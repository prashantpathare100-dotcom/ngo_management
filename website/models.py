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

<<<<<<< HEAD
    @property
    def progress_percent(self):
        try:
            if self.goal_amount and self.goal_amount > 0:
                return int((self.raised_amount / self.goal_amount) * 100)
        except:
            pass
        return 0
    


=======

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
>>>>>>> 200db6d5490057d1df43e554794e297daf680807
