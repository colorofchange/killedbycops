from django.contrib import admin
from tweets.models import Tweet

class TweetAdmin(admin.ModelAdmin):
  raw_id_fields = ('fatal_encounter',)
  list_display = ('fatal_encounter', 'text', 'num_chars_tag', 'location_id', 'image_tag', 'tweet_sent')
  list_filter = ('tweet_sent',)
  search_fields = ('fatal_encounter__name', 'fatal_encounter__city')

admin.site.register(Tweet, TweetAdmin)
