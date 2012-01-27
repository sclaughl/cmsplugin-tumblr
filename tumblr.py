import urllib
import urllib2
import json

base_url = "http://api.tumblr.com/v2/blog/%(base-hostname)s/%(method)s"
api_key = "dABMxJ96CLDzUZzlvyf4rHDGo7Ecr5AtfvR0i9bsBfYJh83xua"
qs_params = { "api_key" : api_key }

def get_avatar(hostname):
	avatar_url = base_url % {
			"base-hostname" : hostname,
			"method" : "avatar" }
	return avatar_url

def get_posts(hostname, tag, limit):
	posts_url = base_url % {
			"base-hostname" : hostname,
			"method" : "posts" }
	posts_url += "?%s" % urllib.urlencode(qs_params)

	response = urllib2.urlopen(posts_url).read()
	return json.loads(response)['response']

