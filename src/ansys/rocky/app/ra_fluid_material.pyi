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

from rocky30.models.material.fluid_material import FluidMaterial as FluidMaterial

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_addins import ElementWithAddins as ElementWithAddins

class RAFluidMaterial(ApiElementItem, ElementWithAddins):
    """
    Rocky PrePost Scripting wrapper for individual fluid materials in a project.

    Retrieve individual materials from the :class:`RAStudy`
    or the :class:`RAMaterialCollection` via:

    .. code-block:: python

        material_1 = study.GetElement('fluid material 1')
        material_2 = material_collection.GetMaterial('fluid material 2')
        material_3 = material_collection[2]
    """

    @classmethod
    def GetWrappedClass(self) -> type[FluidMaterial]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetDensity(self, unit: str | None = None) -> float:
        """
        Get the value of "Density".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "kg/m3".
        """

    def SetDensity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Density".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "kg/m3".
        """

    def GetName(self) -> str:
        """
        Get the value of "Name".

        """

    def SetName(self, value: str) -> None:
        """
        Set the value of "Name".

        :param value:
            The value to set.
        """

    def GetSpecificHeat(self, unit: str | None = None) -> float:
        """
        Get the value of "Specific Heat".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "J/kg.K".
        """

    def SetSpecificHeat(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Specific Heat".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "J/kg.K".
        """

    def GetThermalConductivity(self, unit: str | None = None) -> float:
        """
        Get the value of "Thermal Conductivity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "W/m.K".
        """

    def SetThermalConductivity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Thermal Conductivity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "W/m.K".
        """

    def GetViscosity(self, unit: str | None = None) -> float:
        """
        Get the value of "Viscosity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "Pa.s".
        """

    def SetViscosity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Viscosity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "Pa.s".
        """
