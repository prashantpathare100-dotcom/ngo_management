from django.db import models

# Create your models here.
class Donation(models.Model):
    # cause = models.ForeignKey(Cause, on_delete=models.SET_NULL, null=True, related_name="donations")
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    pan = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  
    cvv =models.IntegerField()
    expiry =models.IntegerField
    cardno =models.IntegerField()


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    
    
class Cause(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    image = models.ImageField(upload_to="causes/", blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    goal_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    raised_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
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