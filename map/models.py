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
        return "%s, %s" % (self.name, self.state)

    class Meta:
        verbose_name_plural = "counties"


class StoryEmbed(models.Model):
    name = models.CharField(max_length=255)
    county = models.ForeignKey(County, null=True)
    image = models.ImageField(upload_to="images/stories")
    url = models.URLField()

    def __unicode__(self):
        return self.name

    def image_tag(self):
        if self.image:
            return "<img src=/media/%s width='100'/>" % self.image
        else:
            return ""
    image_tag.short_description = "Image"
    image_tag.allow_tags = True
