import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(
    name='django-mobile-template',
    version='0.1',
    packages=[
        'mobile_template',
    ],
    include_package_data=True,
    url='https://github.com/linevich/django-mobile-template',
    license='Apache 2.0',
    long_description=README,
    author='Anton Linevych',
    author_email='mail@linevich.net',
    description='Simple app that dynamically changes the templates based on domain/subdomain.',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
