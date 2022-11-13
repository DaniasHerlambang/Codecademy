from django.db import models

# Create your models here.
class Bank_result(models.Model):
    result = models.TextField(null=True, blank=True , editable=True)
    def __str__(self):
        return str(self.result)