from django.db import models

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


class StoryEmbed(models.Model):
    name = models.CharField(max_length=255)
    county = models.ForeignKey(County, null=True)
    url = models.URLField()

    def __unicode__(self):
        return self.name
