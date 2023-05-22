from django.shortcuts import render
from .forms import UserProfileForm

from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def user_profile(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('career_interest')  # redirect to career interest page after form submission
    else:
        form = UserProfileForm()

    return render(request, "resume.html", {"form": form})

def career_interest(request):
    user_profile = UserProfile.objects.last()  # get the last user profile created

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user_profile)  # initialize form with the last user profile and request data
        if form.is_valid():
            form.save()  # update the user profile with the career interest
            # redirect to a new page, or add a success message
    else:
        form = UserProfileForm(instance=user_profile)  # initialize form with the last user profile

    return render(request, "career.html", {"form": form})

