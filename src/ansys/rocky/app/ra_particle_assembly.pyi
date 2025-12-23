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

from collections.abc import Sequence

from rocky30.models.particle.particle_assembly import (
    ParticleAssemblyCustom as ParticleAssemblyCustom,
)
from rocky30.models.particle.particle_assembly import (
    ParticleAssemblyPart as ParticleAssemblyPart,
)
from rocky30.models.particle.particle_assembly import (
    ParticleAssemblyPartList as ParticleAssemblyPartList,
)

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_list import RAList as RAList
from ansys.rocky.app.rocky_api_deprecated_decorator import ApiDeprecated as ApiDeprecated

class RAParticleAssemblyPart(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper for a single entry in a single Particle Assembly's part list.

    Access this wrapper from a given :class:`RAParticleAssembly` with:

    .. code-block:: python

        assembly_parts = particle_assembly.GetAssemblyParts()
        assembly_part_1 = assembly_parts.New()
        assembly_part_1.SetParticle('Particle 1')
        assembly_part_1.SetPositionX(0.75, 'm')
    """

    @classmethod
    def GetWrappedClass(self) -> type[ParticleAssemblyPart]: ...
    @classmethod
    def GetClassName(self): ...
    def GetAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetAngle(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
        """

    def GetPositionX(self, unit: str | None = None) -> float:
        """
        Get the value of "Position X".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetPositionX(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Position X".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetPositionY(self, unit: str | None = None) -> float:
        """
        Get the value of "Position Y".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetPositionY(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Position Y".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetPositionZ(self, unit: str | None = None) -> float:
        """
        Get the value of "Position Z".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetPositionZ(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Position Z".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetRotationX(self, unit: str | None = None) -> float:
        """
        Get the value of "Rotation X".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetRotationX(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Rotation X".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetRotationY(self, unit: str | None = None) -> float:
        """
        Get the value of "Rotation Y".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetRotationY(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Rotation Y".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetRotationZ(self, unit: str | None = None) -> float:
        """
        Get the value of "Rotation Z".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetRotationZ(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Rotation Z".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetScale(self, unit: str | None = None) -> float:
        """
        Get the value of "Scale".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetScale(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Scale".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetParticle(self):
        """
        Get the "Particle".

        :rtype: :class:`RAParticle`
        """

    def SetParticle(self, value) -> None:
        """
        Set the "Particle".

        :param unicode, :class:`RAParticle` value:
            Either the API object wrapping the desired entity or its name.
        """

    def GetAvailableParticles(self):
        """
        Get all available Particles.

        :rtype: List[:class:`RAParticle`]
            A list of :class:`RAParticle`.
        """

class RAParticleAssemblyPartList(RAList[RAParticleAssemblyPart]):
    """
    Rocky PrePost Scripting wrapper for the parts list in a single Particle Assembly.

    To get the :class:`RAParticleAssemblyPartList` from a :class:`RAParticleAssembly`, use:

    .. code-block:: python

        assembly_parts = particle_assembly.GetAssemblyParts()

    :class:`RAParticleAssemblyPartList` contains methods to add, remove and retrieve individual
    assembly parts. It corresponds to the list of entries on a Particle Assembly\'s "Shape" tab
    on the Rocky UI.

    The following examples add, remove and access individual entries in the assembly parts list:

    .. code-block:: python

        # Add new items
        assembly_part_1 = assembly_parts.New()

        # Access and modify items
        assembly_part_2 = assembly_parts[0]
        assembly_part_2.SetParticle(\'Particle 1\')

        # Remove items
        assembly_parts.Remove(assembly_part_2)
        del assembly_parts[0]
        assembly_parts.Clear()

    The :class:`RAParticleAssemblyPartList` is a list of :class:`RAParticleAssemblyPart`.
    """

    @classmethod
    def GetWrappedClass(self) -> type[ParticleAssemblyPartList]: ...
    @classmethod
    def GetClassName(self) -> str: ...

class RAParticleAssemblyCustom(ApiElementItem):
    @classmethod
    def GetWrappedClass(self) -> type[ParticleAssemblyCustom]: ...
    @classmethod
    def GetClassName(self): ...
    def GetMomentOfInertia(self, unit: str | None = None) -> list[float]:
        """
        Deprecated: Use :meth:`GetPrincipalMomentOfInertia()` instead.
        """

    def SetMomentOfInertia(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Deprecated: Use :meth:`SetPrincipalMomentOfInertia()` instead.
        """

    def GetArea(self, unit: str | None = None) -> float:
        """
        Get the value of "Area".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m2".
        """

    def SetArea(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Area".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m2".
        """

    def GetCenterOfMass(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Center of Mass".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetCenterOfMass(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Center of Mass".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetEnabled(self) -> bool:
        """
        Get the value of "Enabled".

        """

    def SetEnabled(self, value: bool) -> None:
        """
        Set the value of "Enabled".

        :param value:
            The value to set.
        """

    def GetGeometricCenter(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Geometric Center".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m".
        """

    def SetGeometricCenter(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Geometric Center".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetInertiaXAxis(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Inertia X Axis".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "-".
        """

    def SetInertiaXAxis(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Inertia X Axis".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "-".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetInertiaYAxis(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Inertia Y Axis".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "-".
        """

    def SetInertiaYAxis(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Inertia Y Axis".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "-".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetInertiaZAxis(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Inertia Z Axis".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "-".
        """

    def SetInertiaZAxis(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Inertia Z Axis".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "-".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetMass(self, unit: str | None = None) -> float:
        """
        Get the value of "Mass".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "kg".
        """

    def SetMass(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Mass".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "kg".
        """

    def GetPrincipalMomentOfInertia(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Principal Moment of Inertia".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "m5".
        """

    def SetPrincipalMomentOfInertia(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Principal Moment of Inertia".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "m5".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetPorosity(self, unit: str | None = None) -> float:
        """
        Get the value of "Porosity".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "<fraction>".
        """

    def SetPorosity(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Porosity".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "<fraction>".
        """

    def GetVolume(self, unit: str | None = None) -> float:
        """
        Get the value of "Volume".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m3".
        """

    def SetVolume(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Volume".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m3".
        """
