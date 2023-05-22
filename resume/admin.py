from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'timestamp')

admin.site.register(UserProfile, UserProfileAdmin)
