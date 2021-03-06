Internationalization
====================

| To internationalize used a standard utility ``gettext`` (http://www.gnu.org/software/gettext/).
| Before you begin, setup it in your system, such as:

.. code-block:: bash
   :caption: debian

   apt-get install gettext
   
.. code-block:: bash
   :caption: nixos

   nix-env -i gettext
   
Also you need ``Babel`` package:

.. code-block:: bash

    pip install babel

:mod:`pyramid_sacrud` has certain labels in templates like "Home", "Create",
"Delete", etc. If these labels appear in English on your admin panel although
you specified another language, then this page is for you.

:mod:`pyramid_sacrud` needs your help for translation of these labels.
Translation process involves the following steps:

Update translatable messages
----------------------------

Execute ``extract_messages`` each time a translatable message text is changed or
added:

.. code-block:: bash

    python setup.py extract_messages

or for linux:

.. code-block:: bash

    make extract_messages

This will create or update ``pyramid_sacrud/locale/pyramid_sacrud.pot`` file,
the central messages catalog used by the different translations.

Create new translation catalog
------------------------------

Execute ``init_catalog`` once for each new language, e.g.:

.. code-block:: bash

    python setup.py init_catalog -l de -i pyramid_sacrud/locale/pyramid_sacrud.pot -o pyramid_sacrud/locale/de/LC_MESSAGES/pyramid_sacrud.po

This will create a file
``pyramid_sacrud/locale/de/LC_MESSAGES/pyramid_sacrud.po`` in which
translations needs to be placed.

Update translation catalog
--------------------------

Execute ``update_catalog`` for each existing language, e.g.:

.. code-block:: bash

    python setup.py update_catalog

or for linux:

.. code-block:: bash

    make update_catalog

This will update file
``pyramid_sacrud/locale/de/LC_MESSAGES/pyramid_sacrud.po`` where translations
of new text needs to be placed.

Compile catalogs
----------------

Execute ``compile_catalog`` for each existing language, e.g.:

.. code-block:: bash

    python setup.py compile_catalog

or for linux:

.. code-block:: bash

    make compile_catalog

Example
-------

English locale by default:

.. figure:: /_static/img/internationalization_en.png

   http://localhost:6543/admin/Catalouge/groups/create/?_LOCALE_=en

Russian locale:

.. figure:: /_static/img/internationalization_ru.png

   http://localhost:6543/admin/Catalouge/groups/create/?_LOCALE_=ru

German locale:

.. figure:: /_static/img/internationalization_de.png

   http://localhost:6543/admin/Catalouge/groups/create/?_LOCALE_=de

.. seealso::

    For more information about Internationalization and Localization read
    official pyramid docs
    http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/i18n.html

    Also see basic settings in `setup.cfg` file
    (hint steal from `here
    <http://babel.edgewall.org/wiki/Documentation/setup.html>`_).

Templates
---------

For translate use `_ps` function:

.. literalinclude:: ../../../pyramid_sacrud/localization/__init__.py
   :linenos:
   :language: py

Example with Jinja2 template:

.. code-block:: html

    <div class="dashboard-title">{{ _ps('Dashboard') }}</div>
    {{ _ps(_(crumb.name)) }}
