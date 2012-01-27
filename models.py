from cms.models import CMSPlugin
from django.db import models

class TumblrPlugin(CMSPlugin):
	hostname = models.CharField(max_length=50)
	tag = models.CharField(max_length=50, help_text="Limits to posts with the specified tag.")
	limit = models.SmallIntegerField(default=20, help_text="Number of posts to return (20 max).")
