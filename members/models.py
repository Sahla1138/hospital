from datetime import date

from django.db import models

class Department(models.Model):
    dep_name = models.CharField(max_length=255)
    dep_description = models.TextField()

    def __str__(self):
        return self.dep_name

class Doctor(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_spec = models.CharField(max_length=255)
    dep_name = models.ForeignKey(Department, on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to = 'doctor')

    def __str__(self):
         return f"{self.doc_name} - {self.doc_spec} - {self.dep_name}"

class Booking(models.Model):
    p_name = models.CharField(max_length=255)
    p_phone= models.CharField(max_length=10)
    p_email = models.EmailField()
    doc_name = models.ForeignKey(Doctor, on_delete=models.CASCADE,
                                     related_name='bookings')

    booking_date = models.DateField(default=date.today)
    booked_on = models.DateTimeField(auto_now_add=True)
    
    
    is_expired = models.BooleanField(default=False)
    
    
    def __str__(self): 
        
        return self.p_name       





    