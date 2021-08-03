# flake8: noqa

from .base import *

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================

CELERY_BROKER_URL = "redis://:p0d1abee82fed2bc830f8c6a9fc25289477c769dfac101496168fed1ebba1a6ca@ec2-54-155-75-145.eu-west-1.compute.amazonaws.com:26789"
