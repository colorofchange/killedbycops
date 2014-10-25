from django.contrib import admin
from tweets.models import Tweet, DoNotSend

class TweetAdmin(admin.ModelAdmin):
  raw_id_fields = ('fatal_encounter',)
  list_display = ('fatal_encounter', 'text', 'num_chars_tag', 'location_id', 'image_tag', 'tweet_sent', 'order')
  list_filter = ('tweet_sent',)
  search_fields = ('fatal_encounter__name', 'fatal_encounter__city', 'text')

class DoNotSendAdmin(admin.ModelAdmin):
  raw_id_fields = ('fatal_encounter',)
  list_display = ('fatal_encounter','reason') 

admin.site.register(Tweet, TweetAdmin)
admin.site.register(DoNotSend, DoNotSendAdmin)