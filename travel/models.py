from django.db import models

# Create your models here.
class Tourist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)
    description = models.TextField(db_column='DESCRIPTIONS', blank=True, null=True)
    location = models.TextField(db_column='LOCATION', blank=True, null=True)
    operating_hours = models.CharField(db_column='OPERATING_HOURS', max_length=255, blank=True, null=True)
    entrance_fee = models.CharField(db_column='ENTRANCE_FEE', max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='tourist_images/', blank=True, null=True)
    parking = models.CharField(db_column='parking', max_length=255, blank=True, null=True)

    class Meta:
        managed = True  # False에서 True로 변경
        db_table = 'tourist'