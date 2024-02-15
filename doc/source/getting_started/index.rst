.. _ref_index_getting_started:

===============
Getting started
===============

PyRocky is a Python client library for remotely controlling
`Ansys Rocky <https://www.ansys.com/products/fluids/ansys-rocky>`_,
which is the most powerful software in the market for performing
DEM (discrete element method) simulations.

Install PyRocky
---------------

PyRocky is currently a private GitHub library in the Ansys Internal account. To
install PyRocky in user mode, run this command:

.. code:: bash

    python -m pip install https://github.com/ansys/pyrocky


Launch PyRocky
--------------

The best way to experiment with PyRocky is by using `Jupyter Notebook <https://jupyter.org/>`_
or `Visual Studio Code <https://code.visualstudio.com>`_. The following code launches a
headless Rocky session and returns a ``RockyClient`` instance from which you can programmatically
interact with the software:

..  code:: python

    import ansys.rocky.rocky as pyrocky

    rocky = pyrocky.launch_rocky()

You use the ``close()`` method to close the Rocky session:

..  code:: python

    rocky.close()

If you want to launch the Rocky UI, set ``headless=False``:

..  code:: python

    rocky = pyrocky.launch_rocky(headless=False)

Connect to an existing session
------------------------------

Assume that a Rocky session is started with the ``--pyrocky`` option:

.. code:: bat

   C:\Program Files\Ansys Inc\v241\Rocky> bin\Rocky.exe --pyrocky

When the Rocky session is started in this way, you can connect to it with PyRocky:

.. code:: python

    import ansys.rocky.rocky as pyrocky

    rocky = pyrocky.connect_to_rocky()
