# django compressor  and less-c compiler

COMPRESS_ENABLED = False
COMPRESS_PRECOMPILERS = (('text/less', 'lessc {infile} {outfile}'),)

# django mobility

# A regex for detecting mobile user agents -- added ipad as mobile!
MOBILE_USER_AGENTS = 'android|fennec|iemobile|iphone|ipad|opera (?:mini|mobi)'
# The name of the cookie to set if the user prefers the mobile site.
MOBILE_COOKIE = 'mobile'


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    # To use the is_desktop context processor, replace app_name and uncomment the following line:
    #'app_name.context_processors.is_desktop',
)
