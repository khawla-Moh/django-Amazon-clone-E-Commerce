from django.db import models

# Create your models here.
class Settings(models.Model):
    name=models.CharField(max_length=100)
    logo=models.ImageField(upload_to="settings")
    subtitle=models.TextField(max_length=500)
    email_us=models.CharField(max_length=30)
    call_us=models.CharField(max_length=30)
    emails=models.CharField(max_length=50)
    phones=models.CharField(max_length=50)
    address=models.TextField(max_length=100)
    android_app=models.URLField(null=True,blank=True)
    iso_app=models.URLField(null=True,blank=True)
    youtube=models.URLField(null=True,blank=True)
    facebook=models.URLField(null=True,blank=True)
    

    def __str__(self):
        return self.name
    


class DeliveryFee(models.Model):
     fee=models.IntegerField()



     def __Str__(self):
            return str(self.fee)
