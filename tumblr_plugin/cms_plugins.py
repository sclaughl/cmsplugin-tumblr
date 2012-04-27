from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import TumblrPlugin
import tumblr

class CMSTumblrPlugin(CMSPluginBase):
    model = TumblrPlugin
    name = "Tumblr"
    render_template = "cms/plugins/tumblr.html"

    def render(self, context, instance, placeholder):
        context.update({
            'tumblr_avatar' : tumblr.get_avatar(instance.hostname),
            'tumblr_content' : tumblr.get_posts(instance.hostname, instance.tag, instance.limit),
        })
        return context

plugin_pool.register_plugin(CMSTumblrPlugin)
