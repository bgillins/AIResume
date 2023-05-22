from django.shortcuts import render
from .forms import UserProfileForm

from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from .AIAssistant import Assistant

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

            # Now, let's get the AI assistant to generate a job description
            assistant = Assistant()
            preferred_job_prompt = assistant.ai_job_focused(form.cleaned_data['career_interest'])
            response = preferred_job_prompt.run(preferred_job_title=form.cleaned_data['career_interest'],
                                                role=assistant.ai_role())

            # Save the response to the session
            request.session['job_description'] = response
            return redirect('job-description')

    else:
        form = UserProfileForm(instance=user_profile)  # initialize form with the last user profile

    return render(request, "career.html", {"form": form})


def job_description(request):
    # Retrieve the job description from the session and render it in the template
    job_description = request.session.get('job_description')
    return render(request, 'job_description.html', {'job_description': job_description})
