from django.contrib import admin
from tweets.models import Tweet

class TweetAdmin(admin.ModelAdmin):
  raw_id_fields = ('fatal_encounter',)

admin.site.register(Tweet, TweetAdmin)
