from django.db import models

class AdminInfo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(upload_to="contact/")
    # photo = models.ImageField(upload_to="contact/", null=True, blank=True)

    # map_embed_url = models.TextField()
    # direction_link = models.CharField(max_length=500)

    card_image = models.ImageField(upload_to="cards/")
    card_title = models.CharField(max_length=200)
    card_details = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    pan = models.CharField(max_length=20, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"

class AdminInfop(models.Model):
    name= models.CharField(max_length=200)
    mobile   = models.CharField(max_length=15, blank=True, null=True)
    email= models.EmailField()
    password = models.CharField(max_length=20)
    gender = models.CharField(max_length=30)
    profile = models.ImageField(upload_to="static/")
    logo = models.ImageField(upload_to="static/")
    facebook= models.CharField(max_length=500)
    instagram= models.CharField(max_length=500)
    linkedin = models.URLField(blank=True, null=True)
    whatsapp = models.CharField(max_length=20, blank=True, null=True)
