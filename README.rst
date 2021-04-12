===================================
Django Component Tags - Tailwindcss
===================================

:Test Status:
    .. image:: https://img.shields.io/github/workflow/status/syse-i/django-component-tags-tailwindcss/Run%20tests
        :alt: GitHub Workflow Status

:Version Info:
    .. image:: https://img.shields.io/pypi/v/django-component-tags-tailwindcss?label=PyPi
        :alt: PyPI

    .. image:: https://img.shields.io/pypi/dm/django-component-tags-tailwindcss?label=Downloads&style=flat-square
        :alt: PyPI - Downloads

:Compatibility:
    .. image:: https://img.shields.io/pypi/pyversions/django-component-tags-tailwindcss?style=flat-square&label=Python%20Versions
        :target: https://pypi.org/project/django-component-tags-tailwindcss/

    .. image:: https://img.shields.io/pypi/djversions/django-component-tags-tailwindcss?label=Django%20Versions&style=flat-square
        :alt: PyPI - Django Version

Tailwindcss component tags for Django Projects.

.. list-table:: Demo
   :widths: 50 50

   * - .. image:: _static/images/Firefox_Screenshot_2021-04-06T18-09-33.871Z.png
            :width: 400
            :alt: Demo 1
     - .. image:: _static/images/Firefox_Screenshot_2021-04-06T18-10-16.796Z.png
            :width: 400
            :alt: Demo 2



Description
===========

Django template tags based on `Tailwindcss <tailwindcss.com/>`_,
created with `django-component-tags <https://github.com/syse-i/django-component-tags>`_.

**Tailwind** is an utility-first CSS framework packed with classes like ``flex, pt-4, text-center and rotate-90``
that can be composed to build any design, directly in your markup.

Requirements
============

Requires Django 2.2 or newer, and is tested against Python 3.7 and PyPy.

Quick Start
============

Install the python package ``django-component-tags-tailwindcss`` from pip:

.. code-block::

    pip install django-component-tags-tailwindcss

Add it to ``INSTALLED_APPS`` in your ``settings.py``:

.. code-block::

    INSTALLED_APPS = [
        ...
        'component_tags',
        'component_tags_tailwindcss',
        ...
    ]
    ...


.. note::

    Check out `component_tags <https://github.com/syse-i/django-component-tags>`_ instructions to complete this installation.

Next, create your own base template:

.. code-block::

    # templates/index.html
    {% load static %}
    {% load tailwindcss_component_tags %}
    <!DOCTYPE html>
    <html lang="en">
    {% block head %}
        <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>-----</title>
            <!-- Styles -->
            <link rel="stylesheet" href="{% static 'component_tags_tailwindcss/css/tailwind.min.css' %}">
            {% components_css %}
        </head>
    {% endblock head %}
    <body>
    {% block content %}{% endblock content %}
    <!-- Scripts -->
    {% components_js %}
    </body>
    </html>

After loading the ``tailwindcss_component_tags library`` you will be able to use any of the
available components inside any template.

**Optional**: You can use the provided base template for a quick setup from ``component_tags_tailwindcss/base.html``:

.. code-block::

    # templates/index.html
    {% extends 'component_tags_tailwindcss/base.html' %}
    {% load tailwindcss_component_tags %}

    {% block content %}
        Content goes here...
    {% endblock content %}

We encourage you to make your own installation of Tailwindcss, do not use this base template on production environments.

.. note::

    Checkout `Tailwindcss documentation <https://tailwindcss.com/docs/installation>`_ for more information.

Components
==========

* Link
* Alert*
* Breadcrumb
* Button
* Card
* Dropdown*
* Label
* Modal*

Some components marked with ``*`` require javascript, therefore i choose AlpineJS
to make the minimal javascript logic.

You can of course extend this components and implement your own javascript framework.

.. note::

    Checkout `AlpineJS documentation <https://github.com/alpinejs/alpine/>`_ for more information.

Examples
========

Here we have just a couple of examples to showcase the code. Checkout the example template
if you want to get more examples.

Alert
-----

.. code-block::

    # templates/index.html
    {% extends 'component_tags_tailwindcss/base.html' %}
    {% load tailwindcss_component_tags %}

    {% block content %}
        {% alert %}Link 1{% endalert %}
        {% alert color="primary" %}Primary link{% endalert %}
        {% alert color="danger" %}Secondary Link{% endalert %}
    {% endblock %}

Card
----

.. code-block::

    # templates/index.html
    {% extends 'component_tags_tailwindcss/base.html' %}
    {% load tailwindcss_component_tags %}

    {% block content %}
        {% card %}
            {% slot 'header' %}
                <img class="w-full"
                     src="https://images.unsplash.com/photo-1593642634524-b40b5baae6bb?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2089&q=80"
                     alt="card-logo">
            {% endslot %}
            Card body
        {% endcard %}
    {% endblock %}

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.0rc2. For details and usage
information on PyScaffold see https://pyscaffold.org/.
