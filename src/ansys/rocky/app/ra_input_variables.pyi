# Copyright (C) 2023 - 2025 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from ansys.rocky.app.api_element_item import ApiElementItem

class RAInputVariables(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for the list of parametric input variables.

    The input variables correspond to the Variables list on the Input tab of a project's
    Expressions/Variables dock. This wrapper can be used to create, remove and list a project's
    input variables.

    Retrieve the :class:`RAInputVariables` through the corresponding :class:`RAProject`.
    Example usage:

    .. code-block:: python

        project = app.GetProject()
        input_variables = project.GetInputVariables()

        input_variables.CreateVariable('a', value=1)
        input_variables.CreateVariable('b', value=2)

        input_variables.RemoveVariable('a')

        for variable in input_variables:
            variable.SetValue(3)

        b = input_variables.GetVariableByName('b')
        b.SetValue(4)
    """

    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def CreateVariable(self, name: str, value: float = 0.0) -> RAParametricVar:
        """
        Create a new input variable. Returns the new variable.

        :param name: The variable's name.
        :param value: The initial value for the variable.
        """

    def RemoveVariable(self, variable: RAParametricVar | str) -> None:
        """
        Remove an input variable.

        :param variable:
            Either an instance of RAParametricVar or the name of the variable to remove.
        """

    def GetVariableByName(self, name: str) -> RAParametricVar:
        """
        Get an existing input variable via its name.

        :param name:
            The input variable's name.
        """

    def __len__(self) -> int: ...
    def __getitem__(self, index): ...
    def __iter__(self): ...

class RAParametricVar(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for a parametric input variable.

    Parametric input variables can be retrieved via a project's :class:`RAInputVariables`. This
    wrapper provides methods to rename the variable and change its value. Example usage:

    .. code-block:: python

        input_variables = project.GetInputVariables()
        variable = input_variables.CreateVariable('a')

        variable.SetName('b')
        variable.SetValue(100)
    """

    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetName(self) -> str:
        """
        Get the variable's name.
        """

    def GetValue(self) -> float:
        """
        Get the variable's current value.
        """

    def SetValue(self, value: float) -> None:
        """
        Set the variable's current value.
        """
