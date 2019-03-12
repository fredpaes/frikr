from django.conf import settings

DEFAULT_LICENSES = (
    ('RIG', 'COPYRIGHT'),
    ('LEF', 'COPYLEFT'),
    ('CC', 'CREATIVE COMMONS')
)

LICENSES = getattr(settings, 'LICENSES', DEFAULT_LICENSES)

BADWORDS = getattr(settings, 'BAD_WORDS', [])