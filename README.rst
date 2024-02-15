PyRocky
=======

|pyansys| |MIT| |python| |pypi| |codecov| |MIT| |black| |pre-commit|

PyRocky is a Python client for Ansys Rocky.

Usage
-----

Installation
^^^^^^^^^^^^

To install PyRocky, run this command:

.. code:: bash

    python -m pip install ansys-rocky-core

Getting started
^^^^^^^^^^^^^^^

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

Connecting to an existing session
*********************************

Assume that a Rocky session is started with the ``--pyrocky`` option:

.. code:: bat

   C:\Program Files\Ansys Inc\v241\Rocky> bin\Rocky.exe --pyrocky

When the session is started in this way, you can connect to it with PyRocky:

.. code:: python

    import ansys.rocky.rocky as pyrocky

    rocky = pyrocky.connect_to_rocky()

Using the Rocky PrePost API
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Most of the Rocky PrePost API is available through the ``api`` object. For example,
the following code creates a project and saves it to disk:

..  code:: python

    api = rocky.api
    project = api.CreateProject()
    study = project.GetStudy()
    study.SetName("My Study")

    api.SaveProject("my-project.rocky"))

To view comprehensive PrePost API documentation, in the Rocky app, select
**Help > Manuals > API PrePost**.

Known issues
************

- When opened with the Rocky UI visible (non-headless mode), PyRocky cannot deal with confirmation
  or error dialogs. For example, a call to the ``CloseProject()`` method asks for confirmation,
  causing PyRocky to freeze until **OK** or **Cancel** is clicked in the Rocky UI.
- PyRocky does not cover the entire Rocky API PrePost functionality. For example, methods still not
   supported include ``GetTimeSet`` and ``GetGridFunction``.


.. BADGES
.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
   :target: https://docs.pyansys.com/
   :alt: PyAnsys

.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT

.. |python| image:: https://img.shields.io/pypi/pyversions/ansys-rocky-core?logo=pypi
   :target: https://pypi.org/project/ansys-rocky-core/
   :alt: Python

.. |pypi| image:: https://img.shields.io/pypi/v/ansys-rocky-core.svg?logo=python&logoColor=white
   :target: https://pypi.org/project/ansys-rocky-core
   :alt: PyPI

.. |codecov| image:: https://codecov.io/gh/ansys/pyrocky/graph/badge.svg?token=UZIC7XT5WE
   :target: https://codecov.io/gh/ansys/pyrocky
   :alt: Codecov

.. |GH-CI| image:: https://github.com/ansys/pyrocky/actions/workflows/ci_cd.yml/badge.svg
   :target: https://github.com/ansys/pyrocky/actions/workflows/ci_cd.yml
   :alt: GH-CI

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
   :target: https://github.com/psf/black
   :alt: Black

.. |pre-commit| image:: https://results.pre-commit.ci/badge/github/ansys/pyrocky/main.svg
   :target: https://results.pre-commit.ci/latest/github/ansys/pyrocky/main
   :alt: pre-commit.ci
