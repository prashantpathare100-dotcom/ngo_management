# from django.db import models

# class Donation(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     amount = models.PositiveIntegerField()
#     cause = models.CharField(max_length=50)
#     message = models.TextField(blank=True)
#     is_approved = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.full_name
from django.db import models

class Donation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    amount = models.PositiveIntegerField()
    cause = models.CharField(max_length=50)
    message = models.TextField(blank=True)

    is_approved = models.BooleanField(default=False)  # ✅ THIS LINE

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
