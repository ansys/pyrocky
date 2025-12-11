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

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_addins import (
    ElementWithAddins as ElementWithAddins,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_solid_material import (
    RASolidMaterial as RASolidMaterial,
)

class RAMaterialsInteraction(ApiElementItem, ElementWithAddins):
    """
    Rocky PrePost Scripting wrapper for the interaction between two materials.

    Retrieve a :class:`RAMaterialsInteraction` from a :class:`RAMaterialsInteractionCollection` and
    two :class:`RASolidMaterial`:

    .. code-block:: python

        material_1 = study.GetElement('Default Particles')
        material_2 = study.GetElement('Default Boundaries')
        interaction_collection = RAMaterialCollection.GetMaterialsInteractionCollection()
        interaction = interaction_collection.GetMaterialsInteraction(material_1, material_2)

    Note that the materials to which a :class:`RAMaterialsInteraction` refers are fixed - while they
    can be retrieved with :meth:`GetFirstMaterial()` and :meth:`GetSecondMaterial()`, they can't
    be set.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetFirstMaterial(self) -> RASolidMaterial:
        """
        Get this interaction's first material.
        """

    def GetSecondMaterial(self) -> RASolidMaterial:
        """
        Get this interaction's second material.
        """

    def GetAdhesiveDistance(self, unit: str | None = None) -> float:
        """
        Get the value of "Adhesive Distance".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetAdhesiveDistance(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Adhesive Distance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetAdhesiveFraction(self, unit: str | None = None) -> float:
        """
        Get the value of "Adhesive Fraction".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetAdhesiveFraction(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Adhesive Fraction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetContactStiffnessMultiplier(self, unit: str | None = None) -> float:
        """
        Get the value of "Contact Stiffness Multiplier".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetContactStiffnessMultiplier(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Contact Stiffness Multiplier".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetRestitutionCoefficient(self, unit: str | None = None) -> float:
        """
        Get the value of "Restitution Coefficient".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetRestitutionCoefficient(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Restitution Coefficient".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetDynamicFriction(self, unit: str | None = None) -> float:
        """
        Get the value of "Dynamic Friction".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetDynamicFriction(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Dynamic Friction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetStaticFriction(self, unit: str | None = None) -> float:
        """
        Get the value of "Static Friction".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetStaticFriction(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Static Friction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetSurfaceEnergy(self, unit: str | None = None) -> float:
        """
        Get the value of "Surface Energy".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "J/m2".
        """

    def SetSurfaceEnergy(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Surface Energy".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "J/m2".
        """

    def GetTangentialStiffnessRatio(self, unit: str | None = None) -> float:
        """
        Get the value of "Tangential Stiffness Ratio".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetTangentialStiffnessRatio(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Tangential Stiffness Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetVelocityExponent(self, unit: str | None = None) -> float:
        """
        Get the value of "Velocity Exponent".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetVelocityExponent(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Velocity Exponent".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetVelocityLimit(self, unit: str | None = None) -> float:
        """
        Get the value of "Velocity Limit".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s".
        """

    def SetVelocityLimit(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Velocity Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s".
        """
