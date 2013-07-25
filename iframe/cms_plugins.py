from logging import getLogger

from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from iframe.models import IframeModel



log = getLogger('iframe.cms_plugins')

class IframePlugin(CMSPluginBase):
    model = IframeModel

    def render(self, request, instance, **kwargs):
        return mark_safe(u'<iframe class="iframe" src="{src}" width="{width}" height="{height}"></iframe>'.format(
            src=escape(instance.src),
            width=instance.width,
            height=instance.height
        ))

plugin_pool.register_plugin(IframePlugin)

