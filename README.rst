=============================
Citi Auth
=============================

.. image:: https://badge.fury.io/py/citi-auth.svg
    :target: https://badge.fury.io/py/citi-auth

.. image:: https://travis-ci.org/citixen/citi-auth.svg?branch=master
    :target: https://travis-ci.org/citixen/citi-auth

.. image:: https://codecov.io/gh/citixen/citi-auth/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/citixen/citi-auth

Companies

Documentation
-------------

The full documentation is at https://citi-auth.readthedocs.io.

Quickstart
----------

Install Citi Auth::

    pip install citi-auth

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'companies.apps.CompaniesConfig',
        ...
    )

Add Citi Auth's URL patterns:

.. code-block:: python

    from companies import urls as companies_urls


    urlpatterns = [
        ...
        url(r'^', include(companies_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
