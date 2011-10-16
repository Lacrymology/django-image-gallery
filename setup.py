#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='image_gallery',
    version='0.0.0',
    author='Tomas Neme',
    author_email='lacrymology@gmail.com',
    url='http://github.com/Lacrymology',
    description = 'Django generic image gallery plugin with support for '
                  'reordering in admin.',
    packages=find_packages(),
    provides=['image_gallery', ],
    include_package_data=True,
    install_requires = [
        'django-inline-ordering',
        'sorl-thumbnail',
        ],
    package_data={
        'image_gallery': [
            'templates/*',
            'static/*',
        ]
    },
)
