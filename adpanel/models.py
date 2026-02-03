from django.db import models

class Donation(models.Model):
    cause_id = models.IntegerField(blank=True, null=True)   # optional (जर cause table नसेल तर)
    name = models.CharField(max_length=120)
from django.db import models

<<<<<<< HEAD

# class Donation(models.Model):
#     cause_id = models.IntegerField(blank=True, null=True)   # optional (जर cause table नसेल तर)
#     name = models.CharField(max_length=120)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     pan = models.CharField(max_length=20, blank=True, null=True)
#     amount = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
=======
# # Contact Hero Section
# class ContactHero(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     image = models.ImageField(upload_to='contact/')
#     is_active = models.BooleanField(default=True)
>>>>>>> 200db6d5490057d1df43e554794e297daf680807

#     def __str__(self):
#         return self.title


# # Contact Information
# class ContactInfo(models.Model):
#     address = models.TextField()
#     phone1 = models.CharField(max_length=20)
#     phone2 = models.CharField(max_length=20, blank=True)
#     email1 = models.EmailField()
#     email2 = models.EmailField(blank=True)
#     working_hours = models.TextField()

#     def __str__(self):
#         return "Contact Information"


# # # Google Map
# class ContactMap(models.Model):
#     map_embed_url = models.TextField()

#     def __str__(self):
#         return "Google Map"


# # # Contact Team
# class ContactTeam(models.Model):
#     name = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     email = models.EmailField()
#     photo = models.ImageField(upload_to='contact/team/')
#     is_active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.name
# class ContactMessage(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     subject = models.CharField(max_length=200)
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
class AdminInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(upload_to="contact/")
    photo = models.ImageField(upload_to="contact/", null=True, blank=True)

    map_embed_url = models.TextField()
    direction_link = models.CharField(max_length=500)

    card_image = models.ImageField(upload_to="cards/")
    card_title = models.CharField(max_length=200)
    card_details = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    pan = models.CharField(max_length=20, blank=True, null=True)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"
