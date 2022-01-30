from django.urls import path, include
from django.contrib.auth.models import User
from hiring.api.views import(
    registration_view, UserLogin, UserLogout, TutorPost, StudentApplication, TutorPostList, StudentList, Studentrequirement
)
from rest_framework.authtoken import views

app_name="hiring"  

urlpatterns=[
    path('register', registration_view, name="register"),
    path('login', UserLogin.as_view(), name="login"), 
    path('logout', UserLogout.as_view(), name="logout"),
    path('tutorpost', TutorPost, name="tutorpost"),
    path('apply', StudentApplication, name="apply"),
    path('viewtutors', TutorPostList.as_view(), name="viewtutors"),
    path('viewstudents', StudentList.as_view(), name="viewstudents"),
    path('studentrequirementpost', Studentrequirement, name="viewstudents"),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]