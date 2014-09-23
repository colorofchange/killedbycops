from django.db import models
from fatalencounters.models import FatalEncounter

class Tweet(models.Model):
  fatal_encounter = models.OneToOneField(FatalEncounter)
  text = models.CharField(max_length=140)
  text_updated = models.BooleanField(default=False)
  created_at = models.DateTimeField(blank=True, auto_now_add=True)
  
  share_image_url = models.URLField(blank=True, null=True)
  location_id = models.CharField(max_length=16, blank=True, null=True, help_text="twitter location id")
  tweet_sent = models.BooleanField(default=False)
  tweet_sent_at = models.DateTimeField(blank=True, null=True)
  tweet_id = models.IntegerField(blank=True, null=True)

  def __unicode__(self):
    return self.text

  def image_tag(self):
    if self.share_image_url:
      return "<a href='%s' target='_blank'><img src=%s width='100'/></a>" % (self.share_image_url,self.share_image_url)
    else:
      return ""
  image_tag.allow_tags = True
