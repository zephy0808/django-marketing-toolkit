SECRET_KEY = 'NOTASECRET'


INSTALLED_APPS = [
    'eti_marketing',
    'eti_marketing.landing_page',
    'ckeditor',
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}


ROOT_URLCONF = 'tests.urls'
