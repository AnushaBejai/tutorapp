from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('login/',loginUser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('register/',registerUser,name='register'),
    path('apply/',applyPage,name='apply'),
    path('tutorpost/',tutorpost,name='tutorpost'),
    path('mypost/', mypost, name='mypost'),
    path('studentrequirement/', studentrequirement, name='studentrequirement'),
    path('requirements/', requirements, name='requirements'),
    path('deletepost/<post_id>', delete_tutorpost, name='deletepost'),
    
    
    
]