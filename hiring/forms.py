from django.forms import ModelForm
from .models import *
class ApplyForm(ModelForm):
    class Meta:
        model=Students
        fields="__all__"

class TutorpostForm(ModelForm):
    class Meta:
        model=TutorPost
        fields="__all__"
        

class StudentPostForm(ModelForm):
    class Meta:
        model=studentpost
        fields="__all__"
        






































#from django.forms import ModelForm
#from .models import StudentUser 
#from django.contrib.auth.models import User


#class user_signupform(ModelForm):
     #class Meta:
         #model = StudentUser
         #fields = '__all__'
     
        

          
