from django.db import models
from django.contrib.auth.models import User 
from django.conf import settings 
from django.db.models.signals import post_save 
from django.dispatch import receiver 
from rest_framework.authtoken.models import Token

# Create your models here.
class TimestampModel(models.Model):
    created_Date = models.DateTimeField(("created_date"), auto_now_add=True)
    updated_Date = models.DateTimeField(("updated_date"), auto_now=True) 
    
    class Meta:
        abstract=True #This model will not be used to create any database table


class Tutor(TimestampModel):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    

    def __str__(self):
        return self.name

class Students(TimestampModel):
    category=(
        ('Male','male'),
        ('Female','female'),
        ('Other','other'),
    )
    name=models.CharField(max_length=200,null=True)
    dob=models.DateField(null=True)
    gender= models.CharField(max_length=200,null=True,choices=category)
    mobile= models.CharField(max_length=12,null=True)
    email= models.CharField(max_length=200,null=True)
    
    tutor=models.ManyToManyField(Tutor,blank=True)
    def __str__(self):
        return self.name 


class TutorPost(TimestampModel): 
    category=(
        ('lower primary','lower primary'),
        ('higher primary','higher primary'),
        ('high school','high school'),
        ('graduation','graduation'),        
    )
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    
    subject=models.CharField(max_length=200,null=True)
    level= models.CharField(max_length=200,null=True, choices=category)
    description=models.CharField(max_length=2000,null=True)
    salary=models.IntegerField(null=True)
    experience=models.IntegerField(null=True)
    
    
 
    def __str__ (self):
        return str(self.tutor) 

class studentpost(TimestampModel): 
    category=(
        ('lower primary','lower primary'),
        ('higher primary','higher primary'),
        ('high school','high school'),
        ('graduation','graduation'),        
    )
    
    name=models.CharField(max_length=200,null=True)
    subject=models.CharField(max_length=200,null=True)
    level= models.CharField(max_length=200,null=True, choices=category)
    description=models.CharField(max_length=2000,null=True)
    salary=models.IntegerField(null=True)
    experience=models.IntegerField(null=True)
    phone=models.CharField(max_length=12,null=True)
    
 
    def __str__ (self):
        return str(self.name) 



#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
     if created: 
         Token.objects.create(user=instance)



































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































    