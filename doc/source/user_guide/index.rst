.. _ref_index_user_guide:

==========
User guide
==========

Use Rocky PrePost Scripting
---------------------------

In its current form, PyRocky is a thin layer that enables remote calls to Rocky using the
PrePost Scripting API. This API is available through the ``RockyClient.api`` object. For
example, the following code creates a project and saves it to disk:

.. vale off
..  code:: python

    rocky = pyrocky.launch_rocky()
    api = rocky.api

    project = api.CreateProject()
    study = project.GetStudy()
    study.SetName("My Study")

    api.SaveProject("my-project.rocky"))
.. vale on

To view comprehensive PrePost Scripting documentation, in the Rocky app, select
**Help > Manuals > PrePost Scripting**.

Most methods of PrePost Scripting, when called through PyRocky, work in exactly the same way
as in the Rocky built-in Python shell. However, there are differences worth noting:

- ``RAStudy.GetTimeSet``: In PyRocky, this method returns a ``numpy.array`` of simulation time
  steps in seconds (instead of a ``TimeSet`` object).
- ``KAElementItem.GetCurve``: This method is not supported by PyRocky. Use the ``GetNumpyCurve``
  method to get resulting curves from study entities.


Known issues
************
- When opened with the Rocky UI visible (non-headless mode), PyRocky cannot deal with confirmation
  or error dialogs. For example, a call to the ``CloseProject()`` method asks for confirmation,
  causing PyRocky to freeze until **OK** or **Cancel** is clicked in the Rocky UI.
