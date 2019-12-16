import os
import sys

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# a clean way to find out if we are in unit test mode
# we look for both direct testing with django and for pytest which is also used by coverage

TESTING = sys.argv[1:2] == ['test'] or sys.argv[0].find('pytest') != -1

# Site
SITE_BASE_URL = 'https://itbi-group.com'  # No trailing slash

TIME_ZONE = 'Asia/Ho_Chi_Minh'

# IDP Details
IDP_NAME = 'IBIT Team'
IDP_LOGO = 'http://www.homecredit.vn/img/logo-hc-main.png'  # Width of 200px at least

# Test service provider
SERVICE_PROVIDER = 'Test service provider'
SERVICE_PROVIDER_URL = 'https://itbi-group.com'

# This setting enables capturing of a users institution and country details
IDP_CATCH_ALL = False

# LDAP Settings

LDAP_PROTO = 'ldap'
# LDAP_HOST = '127.0.0.1'
LDAP_HOST = 'itbi-group.com'
LDAP_PORT = '389'  # must be str
LDAP_BIND_DN = 'cn=admin,dc=itbi-group,dc=com'
LDAP_BASE_DN = 'ou=people,dc=itbi-group,dc=com'
# LDAP_BASE_DN = 'ou=People,dc=itbi-group,dc=com'
LDAP_BIND_DN_CREDENTIAL = 'abc123'
LDAP_GID = "502"  # group ID to add signed up users
LDAP_BASE_UID = 1000  # Integer

# Registration form can be simplified to your real needs. You can optionally
# remove some parts of the form, removing them from the LDAP_USER_DATA list.
#
# LDAP Schema will include all required fields anyway, so you are able to extend
# the registration process in future again, just adding parts you've deleted
# before.

LDAP_USER_DATA = [
    'Personal Data',
    # 'Organization',
    # 'Address',
]
# Password Reset

PASSWORD_RESET_TOKEN_EXPIRY = 2  # Hours

# EMAIL_BACKEND = "anymail.backends.mailgun.EmailBackend"
# ANYMAIL = {
#     "MAILGUN_API_KEY": "<your key>",
# }

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.itbi-group.com'
EMAIL_HOST_USER = 'admin@itbi-group.com'
EMAIL_HOST_PASSWORD = 'itbi@123'
EMAIL_PORT = 587

DEFAULT_FROM_EMAIL = IDP_NAME + ' <admin@itbi-group.com>'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

SETTINGS_EXPORT = [
    'RECAPTCHA_PUBLIC_KEY',
    'IDP_NAME',
    'IDP_LOGO',
    'SERVICE_PROVIDER',
    'SERVICE_PROVIDER_URL',
    'STATIC_URL',
    'LANGUAGE_CODE',
    'SITE_BASE_URL'
]

# reCaptcha to protect registration and password change from robots
# Get keys here: https://www.google.com/recaptcha/admin
# Only reCAPTCHA v2 is supported
# You can use the keys below for testing:

RECAPTCHA_PUBLIC_KEY = '6Le9-ccUAAAAAEONxfu5sMDym-ExJt1OMSp_CIFw'
RECAPTCHA_PRIVATE_KEY = '6Le9-ccUAAAAAJP8GWvG_9bhAAHiS7Q4zpjj1VS3'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']  # Silence checks

# Bootstrap theme
# Optionally, you can chose one of many themes available from https://bootswatch.com/3/

BOOTSTRAP3 = {
    "theme_url": "https://bootswatch.com/3/flatly/bootstrap.min.css",
}


LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/vanducng/git/django-ldap-user-registration/django_ldap_user_registration/logs/app.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

if DEBUG:
    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']
