from cms.models import CMSPlugin
from django.db import models

class TumblrPlugin(CMSPlugin):
    hostname = models.CharField(max_length=50, help_text="The tumblr blog hostname, e.g. greentype.tumblr.com or www.davidslog.com")
    tag = models.CharField(blank=True, max_length=50, help_text="Limits to posts with the specified tag.")
    limit = models.SmallIntegerField(default=20, help_text="Number of posts to return (20 max).")

    def __unicode__(self):
        return self.hostname
