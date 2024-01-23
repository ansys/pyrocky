.. _ref_index_getting_started:

===============
Getting started
===============


Installation
------------

As of now, PyRocky is on private Beta. You can install it straight from the GitHub
repository:

.. code:: bash

    python -m pip install https://github.com/ansys/pyrocky


Launch PyRocky
--------------

The best way to start with **PyRocky** is by using `Jupyter Notebook <https://jupyter.org/>`_
or `VSCode <https://code.visualstudio.com>`_. The following snippet launches a Rocky
headless session and return a ``RockyClient`` instance from which you'll be able to
programmatically interact with the software:

..  code:: python

    import ansys.rocky.rocky as pyrocky

    rocky = pyrocky.launch_rocky()

To close the Rocky session, just use `close()`:

..  code:: python

    rocky.close()

It's also possible to launch Rocky GUI disabling the headless flag:

..  code:: python

    rocky = pyrocky.launch_rocky(headless=False)


Connecting to an existing session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can connect to a Rocky instance as long as it was started with `--pyrocky`
option:

.. code:: bat

   C:\Program Files\Ansys Inc\v241\Rocky> bin\Rocky.exe --pyrocky

.. code:: python

    import ansys.rocky.rocky as pyrocky

    rocky = pyrocky.connect_to_rocky()
