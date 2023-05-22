from django.urls import path
from . import views

urlpatterns = [
    path('resume/', views.user_profile, name='user_profile'),
    path('career/', views.career_interest, name='career_interest'),  # new URL
    path('job-description/', views.job_description, name='job-description'),
]
