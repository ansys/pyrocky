PyRocky
=======

|pyansys| |MIT| |python| |pypi| |codecov| |MIT| |black| |pre-commit|

A Python package to remote control Ansys Rocky.

Usage
-----

Installation
^^^^^^^^^^^^

As of now, PyRocky is on private Beta. You can install it straight from the GitHub
repository:

.. code:: bash

    python -m pip install https://github.com/ansys/pyrocky

Getting Started
^^^^^^^^^^^^^^^

The best way play with **PyRocky** is by using `Jupyer Notebook <https://jupyter.org/>`_
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
************************************

You can connect to a Rocky session as long as the session is started with `--pyrocky`
option:

.. code:: bat

   C:\Program Files\Ansys Inc\v241\Rocky> bin\Rocky.exe --pyrocky

.. code:: python

    import ansys.rocky.rocky as pyrocky

    rocky = pyrocky.connect_to_rocky()


Using Rocky PrePost API
^^^^^^^^^^^^^^^^^^^^^^^^^^

Most of the Rocky PrePost API is available through the ``api`` object. The following
snippet creates new project and save it to disk:

..  code:: python

    api = rocky.api
    project = api.CreateProject()
    study = project.GetStudy()
    study.SetName("My Studyy")

    api.SaveProject("my-project.rocky"))

You can get the full documentation within Rocky Application (*Help* - *Manuals* -
*API PrePost*).

Known Issues
**************

 - When opened with UI visible (non-headless), PyRocky cannot deal with confirmation
   or error dialogs (for instance, a call to ``CloseProject()`` will ask for confirmation
   and PyRocky will freeze until user click `OK` or `Cancel` on the UI).
 - Some API methods may not work.

.. LINKS AND REFERENCES
.. _black: https://github.com/psf/black
.. _flake8: https://flake8.pycqa.org/en/latest/
.. _isort: https://github.com/PyCQA/isort
.. _pip: https://pypi.org/project/pip/
.. _pre-commit: https://pre-commit.com/
.. _PyAnsys Developer's guide: https://dev.docs.pyansys.com/
.. _pytest: https://docs.pytest.org/en/stable/
.. _Sphinx: https://www.sphinx-doc.org/en/master/
.. _tox: https://tox.wiki/

.. BADGES
.. |pyansys| image:: https://img.shields.io/badge/Py-Ansys-ffc107.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAIAAACQkWg2AAABDklEQVQ4jWNgoDfg5mD8vE7q/3bpVyskbW0sMRUwofHD7Dh5OBkZGBgW7/3W2tZpa2tLQEOyOzeEsfumlK2tbVpaGj4N6jIs1lpsDAwMJ278sveMY2BgCA0NFRISwqkhyQ1q/Nyd3zg4OBgYGNjZ2ePi4rB5loGBhZnhxTLJ/9ulv26Q4uVk1NXV/f///////69du4Zdg78lx//t0v+3S88rFISInD59GqIH2esIJ8G9O2/XVwhjzpw5EAam1xkkBJn/bJX+v1365hxxuCAfH9+3b9/+////48cPuNehNsS7cDEzMTAwMMzb+Q2u4dOnT2vWrMHu9ZtzxP9vl/69RVpCkBlZ3N7enoDXBwEAAA+YYitOilMVAAAAAElFTkSuQmCC
   :target: https://docs.pyansys.com/
   :alt: PyAnsys

.. |MIT| image:: https://img.shields.io/badge/License-MIT-yellow.svg
   :target: https://opensource.org/licenses/MIT
   :alt: MIT

.. |python| image:: https://img.shields.io/pypi/pyversions/ansys-geometry-core?logo=pypi
   :target: https://pypi.org/project/ansys-geometry-core/
   :alt: Python

.. |pypi| image:: https://img.shields.io/pypi/v/ansys-geometry-core.svg?logo=python&logoColor=white
   :target: https://pypi.org/project/ansys-geometry-core
   :alt: PyPI

.. |codecov| image:: https://codecov.io/gh/ansys/pyansys-geometry/graph/badge.svg?token=UZIC7XT5WE
   :target: https://codecov.io/gh/ansys/pyansys-geometry
   :alt: Codecov

.. |GH-CI| image:: https://github.com/ansys/pyansys-geometry/actions/workflows/ci_cd.yml/badge.svg
   :target: https://github.com/ansys/pyansys-geometry/actions/workflows/ci_cd.yml
   :alt: GH-CI

.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=flat
   :target: https://github.com/psf/black
   :alt: Black

.. |pre-commit| image:: https://results.pre-commit.ci/badge/github/ansys/pyansys-geometry/main.svg
   :target: https://results.pre-commit.ci/latest/github/ansys/pyansys-geometry/main
   :alt: pre-commit.ci
