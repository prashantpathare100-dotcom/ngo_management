from django.db import models




# class Donation(models.Model):
#     cause_id = models.IntegerField(blank=True, null=True)   # optional (जर cause table नसेल तर)
#     name = models.CharField(max_length=120)
#     email = models.EmailField()
#     phone = models.CharField(max_length=20)
#     pan = models.CharField(max_length=20, blank=True, null=True)
#     amount = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.name} - {self.amount}"
