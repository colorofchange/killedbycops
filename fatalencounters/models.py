from django.db import models

class FatalEncounter(models.Model):
  #fields from fatal encounters data
  name = models.CharField(max_length=255)
  age = models.IntegerField(null=True)
  gender = models.CharField(null=True, max_length=1, choices=(('M','Male'),('F','Female')))
  race = models.CharField(null=True, max_length=100)
  photo_url = models.URLField(blank=True, null=True)
  date_of_injury = models.DateField(null=True)
  city = models.CharField(max_length=255, null=True)
  state = models.CharField(max_length=2, null=True)
  agency_responsible = models.CharField(max_length=255, null=True)
  source_url = models.URLField(null=True)
  uid = models.CharField(max_length=10, unique=True)

  def __unicode__(self):
    return self.name

  def photo_tag(self):
    if self.photo_url:
      return "<img src=%s width='100'/>" % self.photo_url
    else:
      return ""
  photo_tag.allow_tags = True