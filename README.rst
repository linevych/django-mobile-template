Django-mobile-template
----------------------

.. image:: https://travis-ci.org/linevich/django-mobile-template.svg?branch=master
    :target: https://travis-ci.org/linevich/django-mobile-template

Simple django app that dynamically change :code:`template_name` of your view based on domain name
(e.g example.com and m.example.com).

Useful in case if you already have third party service that redirects to the mobile version of your site.

Installation
============

.. code-block:: bash

    pip install django-mobile-template
    # OR
    pip install git+https://github.com/linevich/django-mobile-template.git

.. code-block:: python

    INSTALLED_APPS = [
    ...
    'mobile_template',
    ...
    ]

Usage
=====

Please note: :code:`MobileTemplateView` should be **first parent class**.

.. code-block:: python

    # views.py

    from django.views.generic import TemplateView
    from mobile_template.views import MobileTemplateView


    class Home(MobileTemplateView, TemplateView):
        template_name = 'index.html'

Templates folder structure:

.. code-block::

    templates
    ├── base.html
    ├── index.html
    └── mobile
        └── index.html


Configuration
=============

- :code:`MOBILE_TEMPLATES_PREFIX` (Default: :code:`mobile/`) — mobile templates subfolder.
- :code:`MOBILE_DOMAIN_REGEX` (Default: :code:`^m.\.*.\.*.*'`) — regular expression to capture mobile domains.
  By default it captures all domains started with m.<domain_or_subdomain>.



