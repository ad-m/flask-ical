===============================
Flask-iCal
===============================

A simple convert iCalendar to HTML files


Quickstart
----------

First, set your app's secret key as an environment variable. For example, example add the following to ``.bashrc`` or ``.bash_profile``.

.. code-block:: bash

    export FLASK_ICAL_SECRET='something-really-secret'


Then run the following commands to bootstrap your environment.


::

    git clone https://github.com/ad-m/flask-ical
    cd flask-ical
    pip install -r requirements/dev.txt
    python manage.py server

You will see a pretty welcome screen.

Once you have installed your DBMS, run the following to create your app's database tables and perform the initial migration:

::

    python manage.py db init
    python manage.py server



Deployment
----------

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

In your production environment, make sure the ``FLASK_ICAL_ENV`` environment variable is set to ``"prod"``.


Shell
-----

To open the interactive shell, run ::

    python manage.py shell

By default, you will have access to ``app``.


Running Tests
-------------

To run all tests, run ::

    python manage.py test
