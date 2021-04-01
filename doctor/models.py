from django.db import models

# Create your models here.
class doctor(models.Model):
    doctor_id=models.AutoField
    name= models.CharField(max_length=50, default="")
    speciality= models.CharField(max_length=50, default="")
    city= models.CharField(max_length=50, default="")
    area= models.CharField(max_length=50, default="")
    region=models.CharField(max_length=50, default="")
    fees=models.IntegerField(default=0)
    visitingtime=models.CharField(max_length=300, default="")
    shortdiscription=models.CharField(max_length=10000, default="")
    Email=models.CharField(max_length=50, default="")
    phone=models.CharField(max_length=50, default="")
    
    Dateofbirth=models.DateField()
    image= models.ImageField(upload_to="doctor/images",default="")

    def __str__(self):
        return self.name