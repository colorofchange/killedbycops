from django.db import models

class FatalEncounter(models.Model):
  #fields from fatal encounters data
  name = models.CharField(max_length=255)
  age = models.IntegerField(null=True)
  gender = models.CharField(null=True, max_length=1, choices=(('M','Male'),('F','Female')))
  race = models.CharField(null=True, max_length=100)
  photo_url = models.URLField(blank=True, null=True, max_length=1000)
  date_of_injury = models.DateField(null=True)
  city = models.CharField(max_length=255, null=True)
  county = models.CharField(max_length=255, null=True)
  state = models.CharField(max_length=2, null=True)
  agency_responsible = models.CharField(max_length=255, null=True)
  source_url = models.URLField(null=True, max_length=1000)
  proofed = models.BooleanField(default=False)

  def __unicode__(self):
    return self.name

  def photo_tag(self):
    if self.photo_url:
      return "<img src=%s width='100'/>" % self.photo_url
    else:
      return ""
  photo_tag.short_description = "Photo"
  photo_tag.allow_tags = True

  def county_fips(self):
    for n in COUNTY_NAME_TYPES:
      cleaned_name = self.county.replace(n,'')
    try:
      c = County.objects.get(state=self.state,name__startswith=cleaned_name)
      return c.fips_code()
    except County.DoesNotExist:
      return None
    except County.MultipleObjectsReturned:
      try:
        #try exact match
        c = County.objects.get(state=self.state,name=cleaned_name)
        return c.fips_code()
      except County.DoesNotExist:
        return "no exact match"
    return None

COUNTY_NAME_TYPES = ('County', 'Parish', 'Borough', 'Census Area', 'Municipality')

class County(models.Model):
  state = models.CharField(max_length=2)
  state_ansi = models.CharField(max_length=2)
  county_ansi = models.CharField(max_length=3)
  name = models.TextField(max_length=255)

  def fips_code(self):
    return "%s%s" % (self.state_ansi, self.county_ansi)

  def __unicode__(self):
    return self.name

  class Meta:
    verbose_name_plural = "counties"