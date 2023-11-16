.. _ref_index_user_guide:

==========
User Guide
==========


Using Rocky PrePost API
-----------------------

Most of the Rocky PrePost API is available through the ``api`` object. The following
snippet creates new project and save it to disk:

..  code:: python

    api = rocky.api
    project = api.CreateProject()
    study = project.GetStudy()
    study.SetName("My Study")

    api.SaveProject("my-project.rocky"))

You can get the full documentation within Rocky Application (*Help* - *Manuals* -
*API PrePost*).


Known Issues
**************

 - When opened with UI visible (non-headless), PyRocky cannot deal with confirmation
   or error dialogs (for instance, a call to ``CloseProject()`` will ask for confirmation
   and PyRocky will freeze until user click `OK` or `Cancel` on the UI).
 - Some API methods may not work.
