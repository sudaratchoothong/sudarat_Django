from django.db import models

# Create your models here.
    
class sudarat_tb_model(models.Model):
    member_studentId = models.CharField(max_length=200)
    member_firstname = models.CharField(max_length=200)
    member_lastname = models.CharField(max_length=200)
    member_detail = models.TextField() 
    member_image = models.ImageField(upload_to='photo',default='')