from django.contrib import admin

# Register your models here.
from .forms import TweetModelForm
from .models import Tweet


#admin.site.register(Tweet)


class TweetModelAdmin(admin.ModelAdmin):
    #form = TweetModelForm
    list_display = ["user", "id", "content"]
    class Meta:
        model = Tweet

admin.site.register(Tweet, TweetModelAdmin)
