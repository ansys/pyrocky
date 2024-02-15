.. _ref_index_user_guide:

==========
User guide
==========


Use the Rocky PrePost API
-------------------------

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
- Some API methods may not work.
