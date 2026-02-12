
Create a Rocky/FreeFlow Docker container
========================================

Requirements
============

* A Linux machine or WSL with `Docker <https://www.docker.com>`_ installed.

* A valid Ansys account.

Procedure
=========

Download Ansys Products
--------------------------------------------

Both Rocky/Freeflow and Ansys License Manager for the desired version can be downloaded from
the `Ansys Customer Portal <https://download.ansys.com>`_.

*Note: Be sure to select Linux x64 as the operating system.*

Install Rocky/FreeFlow
----------------------

The installation consists of unpacking both the downloaded Rocky/FreeFlow archive and the licensing client to the **/ansys_inc/v<version>** directory.

For example, to create a FreeFlow 25.2.3 container, the following folder structure is expected:

.. code:: text

    /ansys_inc
    └── v252
        ├── freeflow
        |   └── <FreeFlow installation files>
        └── licensingclient
            └── <Ansys Licensing client files>

*Note: The licensing client archive can be found on the `clclient` folder of the downloaded Ansys License Manager archive.*

Refer to the `Ansys Products Linux Installation Guide <https://ansyshelp.ansys.com/Views/Secured/corp/v2523/en/ai_instl/install_linux.html>`_
for more information.


Build Docker image
------------------

To build the image, simply run the helper python script `docker/build_image.py <https://github.com/ansys/pyrocky/tree/main/docker/build_image.py>`_.

For example, building a FreeFlow 25.2.3 image from the root of the repository:

.. code:: bash

    python docker/build_image.py --tag freeflow:25.2.3

By default, the script will look for the Dockerfile in the `docker/<version>/<product>/Dockerfile` folder.
If your Dockerfile is located elsewhere, you can specify its path using the ``--dockerfile`` argument:

.. code:: bash

    python docker/build_image.py --tag freeflow:25.2.3 --dockerfile /path/to/Dockerfile
