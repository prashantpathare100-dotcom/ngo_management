from django.db import models

# 1. Hero Section
class ContactHero(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='contact/hero/')

    def __str__(self):
        return self.title


# 2. Contact Information
class ContactInfo(models.Model):
    address = models.TextField()
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20, blank=True)
    email1 = models.EmailField()
    email2 = models.EmailField(blank=True)
    working_hours = models.CharField(max_length=200)

    def __str__(self):
        return self.email1


# 3. Google Map
class GoogleMap(models.Model):
    map_iframe = models.TextField()

    def __str__(self):
        return "Google Map"


# 4. Team Members
class ContactTeam(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    email = models.EmailField()
    image = models.ImageField(upload_to='contact/team/')

    def __str__(self):
        return self.name


# 5. Contact Messages
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
