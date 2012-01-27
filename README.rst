A django-cms plugin that displays the last number of posts of a tumblr user.

This plugin could use a little more fleshing out, but what's there is solid and done properly. It retrieves tumblr data from tumblr's v2 API. It uses only the ``/avatar`` and ``/posts`` methods, thereby avoiding the complexities of oAuth (and the other methods don't really make sense in the context of a CMS plugin anyway). The data returned by the tumblr API are documented at http://www.tumblr.com/docs/en/api/v2/.

Feel free to email me with questions / feature requests.
