from django.db import models


class URL(models.Model):
    long_url   = models.CharField(unique=True, max_length=2000)
    token      = models.CharField(max_length=7)
    created_at = models.DateField(auto_now=True)
    expiry_at  = models.DateField()

    class Meta:
        db_table = 'URL'
