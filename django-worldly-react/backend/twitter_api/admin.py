from django.contrib import admin

from .models import Twitter

class TwitterAdmin(admin.ModelAdmin):
    list_display = ('tweet_id', 'text')

# Register your models here.

admin.site.register(Twitter, TwitterAdmin)

# Register your models here.
