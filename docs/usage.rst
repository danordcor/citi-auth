=====
Usage
=====

To use Citi Auth in a project, add it to your `INSTALLED_APPS`:

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
