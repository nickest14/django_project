from django.contrib import admin

# Register your models here.

from .models import UserProfile

class UserModelAdmin(admin.ModelAdmin):
    list_display = ["user"]
    # list_display_links
    # list_filter
    # list_editable
    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserModelAdmin)
