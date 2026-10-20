# Copyright (C) 2023 - 2026 Synopsys, Inc. and ANSYS, Inc. All rights reserved.
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

from typing import Any

from _typeshed import Incomplete
from rocky30.models.material.fluid_material import FluidMaterial as FluidMaterial
from rocky30.models.material.fluid_material import (
    HerschelBulkleyRheologicalModel as HerschelBulkleyRheologicalModel,
)
from rocky30.models.material.fluid_material import (
    NewtonianRheologicalModel as NewtonianRheologicalModel,
)
from rocky30.models.material.fluid_material import (
    RheologicalModelType as RheologicalModelType,
)

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_addins import ElementWithAddins as ElementWithAddins
from ansys.rocky.app.rocky_api_deprecated_decorator import ApiDeprecated as ApiDeprecated

class RAHerschelBulkleyRheologicalModel:
    @classmethod
    def GetWrappedClass(self) -> type[HerschelBulkleyRheologicalModel]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    subject: Incomplete
    def __init__(self, rheological_model: Any) -> None: ...
    def GetBehaviorIndex(self) -> float:
        """
        Get the value of "Behavior Index".

        """

    def SetBehaviorIndex(self, value: str | float) -> None:
        """
        Set the value of "Behavior Index".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetMaximumViscosity(self, unit: str | None = None) -> float:
        """
        Get the value of "Maximum Viscosity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "Pa.s".
        """

    def SetMaximumViscosity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Maximum Viscosity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "Pa.s".
        """

    def GetReferenceViscosity(self, unit: str | None = None) -> float:
        """
        Get the value of "Reference Viscosity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "Pa.s".
        """

    def SetReferenceViscosity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Reference Viscosity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "Pa.s".
        """

    def GetYieldStress(self, unit: str | None = None) -> float:
        """
        Get the value of "Yield Stress".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "Pa".
        """

    def SetYieldStress(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Yield Stress".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "Pa".
        """

class RANewtonianRheologicalModel:
    subject: Incomplete
    def __init__(self, rheological_model: Any) -> None: ...
    @classmethod
    def GetWrappedClass(self) -> type[NewtonianRheologicalModel]: ...
    @classmethod
    def GetClassName(self) -> str: ...
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
    def GetNewtonianRheologicalModel(self) -> RANewtonianRheologicalModel: ...
    def GetHerschelBulkleyRheologicalModel(self) -> RAHerschelBulkleyRheologicalModel: ...
    def GetRheologicalModel(self) -> object: ...
    def GetRheologicalModelType(self) -> str:
        """
        Get "Rheological Model Type" as a string.

        :return:
            The returned value will be one of [\'newtonian\', \'herschel_bulkley_papanastasiou\'].
        """

    def SetRheologicalModelType(self, value: str) -> None:
        """
        Set the value of "Rheological Model Type".

        :param value:
            The value to set. Must be one of [\'newtonian\', \'herschel_bulkley_papanastasiou\'].
        :raises RockyApiError:
            If `value` is not a valid "Rheological Model Type" option.
        """

    def GetValidRheologicalModelTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Rheological Model Type".

        :return:
            The returned list is [\'newtonian\', \'herschel_bulkley_papanastasiou\'].
        """

    def GetViscosity(self, unit: str | None = None) -> float: ...
    def SetViscosity(self, value: str | float, unit: str | None = None) -> None: ...
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
