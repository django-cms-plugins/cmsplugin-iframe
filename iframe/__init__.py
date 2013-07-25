from django.conf import settings



if 'cmsplugin_iframe' in settings.INSTALLED_APPS:
    if not hasattr(settings,'CMS_PLUGIN_IFRAME_MEDIA_URL'):
        settings.CMS_PLUGIN_IFRAME_MEDIA_URL = settings.MEDIA_URL + 'cmsplugin_iframe/'
