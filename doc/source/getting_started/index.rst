.. _ref_index_getting_started:

===============
Getting started
===============


Installation
------------

PyRocky is currently a private library in the Ansys Internal GitHub account. To
install PyRocky, run this command:

.. code:: bash

    python -m pip install https://github.com/ansys/pyrocky


Launch PyRocky
--------------

The best way to experiment with PyRocky is by using `Jupyter Notebook <https://jupyter.org/>`_
or `Visual Studio Code <https://code.visualstudio.com>`_. The following code launches a Rocky
headless Rocky session and returns a ``RockyClient`` instance from which you can programmatically
interact with the software:

..  code:: python

    import ansys.rocky.rocky as pyrocky

    rocky = pyrocky.launch_rocky()

You use the `close()` method to close the Rocky session:

..  code:: python

    rocky.close()

If you want to launch the Rocky GUI, you set ``headless=False``:

..  code:: python

    rocky = pyrocky.launch_rocky(headless=False)

Connecting to an existing session
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Assume that a Rocky session is started with the `--pyrocky` option:

.. code:: bat

   C:\Program Files\Ansys Inc\v241\Rocky> bin\Rocky.exe --pyrocky

When a Rocky session is started in this way, you can connect to it with PyRocky:

.. code:: python

    import ansys.rocky.rocky as pyrocky

    rocky = pyrocky.connect_to_rocky()
