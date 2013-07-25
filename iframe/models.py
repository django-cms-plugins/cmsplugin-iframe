from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin



class IframeModel(CMSPlugin):
    """
    An ''<iframe>'' displayed on the page.
    """

    src = models.URLField(_("Page URL"))
    width = models.CharField(_("Width"), max_length=10, 
            default="100%", 
            help_text=_("Specify the width in pixels, or a percentage."))
    height = models.CharField(_("Height"), max_length=10,
            default="400",
            help_text=_("Specify the height in pixels."))

    class Meta:
        verbose_name = _("Iframe")
        verbose_name_plural = _("Iframes")

    def __unicode__(self):
        return self.src

