=====
Django-authy
=====

Authy is a app for authenticate user in django apps

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "authy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'authy',
    )

2. Include the authy URLconf in your project urls.py like this::

    url(r'^', include('authy.urls')),

3. Run `python manage.py migrate authy` to create the authy models.

