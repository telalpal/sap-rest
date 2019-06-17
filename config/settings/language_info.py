import django.conf.locale


def gettext_noop(s: str) -> str:
    return s


# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-LANGUAGES
LANGUAGES = [
    ('eng', gettext_noop('English')),
    ('spa', gettext_noop('Spanish')),
    ('nso', gettext_noop('Northern Sotho')),
    ('afr', gettext_noop('Afrikaans')),
    ('tsn', gettext_noop('Tswana')),
    ('zul', gettext_noop('Zulu')),
    ('por', gettext_noop('Portuguese')),
    ('sot', gettext_noop('Sotho')),
    ('xho', gettext_noop('Xhosa')),
]

EXTRA_LANG_INFO = {
    'eng': {
        'bidi': False,  # left-to-right
        'code': 'eng',
        'name': 'English',
        'name_local': 'English',
    },
    'spa': {
        'bidi': True,
        'code': 'spa',
        'name': 'Spanish',
        'name_local': u'español',
    },
    'nso': {
        'bidi': True,
        'code': 'nso',
        'name': 'Northern Sotho',
        'name_local': u'Sesotho sa Leboa',
    },
    'afr': {
        'bidi': True,
        'code': 'afr',
        'name': 'Afrikaans',
        'name_local': 'Afrikaans taal',
    },
    'tsn': {
        'bidi': True,
        'code': 'tsn',
        'name': 'Tswana',
        'name_local': 'Tswana',
    },
    'zul': {
        'bidi': True,
        'code': 'zul',
        'name': 'Zulu',
        'name_local': 'Zulu',
    },
    'por': {
        'bidi': True,
        'code': 'por',
        'name': 'Portuguese',
        'name_local': 'Portuguese',
    },
    'sot': {
        'bidi': True,
        'code': 'sot',
        'name': 'Sotho',
        'name_local': 'Sotho',
    },
    'xho': {
        'bidi': True,
        'code': 'xho',
        'name': 'Xhosa',
        'name_local': 'Xhosa',
    },

}

# Add custom languages not provided by Django
LANG_INFO = dict(django.conf.locale.LANG_INFO, **EXTRA_LANG_INFO)
django.conf.locale.LANG_INFO = LANG_INFO
