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

from _typeshed import Incomplete
from rocky30.models.particle.particle_geometry import (
    ParticleShapeTypes as ParticleShapeTypes,
)

from ansys.rocky.app._ra_orientation_mixin import _RAOrientationMixin
from ansys.rocky.app.ra_addins import ElementWithAddins as ElementWithAddins
from ansys.rocky.app.ra_api import RockyApiError as RockyApiError
from ansys.rocky.app.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.app.ra_particle_assembly import (
    RAParticleAssemblyCustom as RAParticleAssemblyCustom,
)
from ansys.rocky.app.ra_particle_assembly import (
    RAParticleAssemblyPartList as RAParticleAssemblyPartList,
)
from ansys.rocky.app.ra_size_distribution import (
    RASizeDistributionList as RASizeDistributionList,
)
from ansys.rocky.app.rocky_api_deprecated_decorator import ApiDeprecated as ApiDeprecated

class RAParticle(RAGridProcessElementItem, ElementWithAddins, _RAOrientationMixin):
    """
    Rocky PrePost Scripting wrapper for a particle in the project.

    The wrapper corresponds to an individual Particle entry in the project\'s data tree, below the
    "Particles" item. Particles can be retrieved from the :class:`RAStudy` or the
    :class:`RAParticleCollection` via:

    .. code-block:: python

        particle_1 = study.GetElement(\'Particle 1\')
        particle_2 = particle_collection[1]
        particle_3 = particle_collection.GetParticle(\'Particle 3\')

    Most particle properties, such as name, shape, aspect ratios, etc can be set directly via methods
    in this wrapper class. An exception is size-related methods, which must be configured via the
    :class:`RASizeDistributionList` returned in :meth:`GetSizeDistributionList()`.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def ImportFromSTL(
        self, stl_filename: str, as_concave: bool, is_open: bool = False
    ) -> bool:
        """
        Import a custom shape from the given stl filename into this particle.

        :param stl_filename:
            The full path to the STL file.
        :param as_concave:
            True whether the particle should be treated as Concave, or False otherwise

        :param is_open:
            True whether the stl is an open one

        :returns:
            Possible return values:
            * True if everything went fine with the import process.
            * False if the import process failed.
        """

    def ImportCustomFiber(self, filename: str) -> bool:
        """
        Import a custom fiber shape from the given filename into this particle.

        :param filename:
            The full path to the TXT/CSV/Excel file.

        :returns:
            Whether it was possible to import the particle
        """

    def GetSizeDistributionList(self) -> RASizeDistributionList:
        """
        Get a list of size distribution entries
        """

    def GetUseMultipleElements(self) -> bool:
        """
        Whether the particle\'s Composition is "Multiple Elements".
        """

    def SetUseMultipleElements(self, value) -> None:
        """
        Set the particle\'s Composition to "Multiple Elements" (True) or "Single Elements" (False).

        :param bool value:
        """

    def IsConcave(self):
        """
        Returns True if the particle is a concave custom polyhedron, and False otherwise.

        :rtype: bool
        """

    def GetBreakageModel(self) -> str:
        """
        This docstring is overridden by the _GetBreakageModel's at the end of the file.
        """

    def GetValidBreakageModelValues(self) -> list[str]:
        """
        This docstring is overridden by the _GetValidBreakageModelValues's at the end of the file.
        """

    def SetBreakageModel(self, value: str) -> None:
        """
        Set the value of "Breakage Model".
        If the particle is not flexible, setting the model to any value other than "none" also enables breakage.

        :param str value:
            The value to set. Must be one of [\'none\', \'ab_t10\', \'professor_tavares\', \'instantaneous_custom\', \'griffith_surface_energy\', \'shear_stress_criterion\', \'tensile_stress_criterion\', \'tensile_or_shear_criterion\', \'von_mises_stress_criterion\', \'discrete_custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Breakage Model" option.
        """

    def GetAssemblyParts(self) -> RAParticleAssemblyPartList: ...
    def GetAssemblyCustom(self) -> RAParticleAssemblyCustom:
        """
        Deprecated: Use :meth:`GetCustomProperties()` instead.
        """

    def GetCustomProperties(self) -> RAParticleAssemblyCustom: ...
    def GetAbt10MaximumT10Value(self, unit: str | None = None) -> float:
        """
        Get the value of "Abt10 Maximum T10 Value".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "%".
        """

    def SetAbt10MaximumT10Value(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Abt10 Maximum T10 Value".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "%".
        """

    def GetAbt10ReferenceMinimumSpecificEnergy(self, unit: str | None = None) -> float:
        """
        Get the value of "Abt10 Reference Minimum Specific Energy".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "J/kg".
        """

    def SetAbt10ReferenceMinimumSpecificEnergy(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Abt10 Reference Minimum Specific Energy".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "J/kg".
        """

    def GetAbt10MinimumSpecificEnergy(self, unit: str | None = None) -> float:
        """
        Deprecated: Use :meth:`GetAbt10ReferenceMinimumSpecificEnergy()` instead.

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "J/kg".
        """

    def SetAbt10MinimumSpecificEnergy(
        self, value: float, unit: str | None = None
    ) -> None:
        """
        Deprecated: Use :meth:`SetAbt10ReferenceMinimumSpecificEnergy()` instead.

        :param value:
            The value to set.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "J/kg".
        """

    def GetAbt10ReferenceSize(self, unit: str | None = None) -> float:
        """
        Get the value of "Abt10 Reference Size".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetAbt10ReferenceSize(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Abt10 Reference Size".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetAbt10SelectFunctionCoefficient(self, unit: str | None = None) -> float:
        """
        Get the value of "Abt10 Select Function Coefficient".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "kg/J".
        """

    def SetAbt10SelectFunctionCoefficient(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Abt10 Select Function Coefficient".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "kg/J".
        """

    def GetDistributionModel(self) -> str:
        """
        Get "Distribution Model" as a string.

        :return:
            The returned value will be one of [\'gaudin_schumann\', \'incomplete_beta\', \'custom\'].
        """

    def SetDistributionModel(self, value: str) -> None:
        """
        Set the value of "Distribution Model".

        :param value:
            The value to set. Must be one of [\'gaudin_schumann\', \'incomplete_beta\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Distribution Model" option.
        """

    def GetValidDistributionModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Distribution Model".

        :return:
            The returned list is [\'gaudin_schumann\', \'incomplete_beta\', \'custom\'].
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

    def GetIncludeRotationalDeformations(self) -> bool:
        """
        Get the value of "Include Rotational Deformations".

        """

    def SetIncludeRotationalDeformations(self, value: bool) -> None:
        """
        Set the value of "Include Rotational Deformations".

        :param value:
            The value to set.
        """

    def EnableIncludeRotationalDeformations(self) -> None:
        """
        Set the value of "Include Rotational Deformations" to True.
        """

    def DisableIncludeRotationalDeformations(self) -> None:
        """
        Set the value of "Include Rotational Deformations" to False.
        """

    def IsIncludeRotationalDeformationsEnabled(self) -> bool:
        """
        Check if the "Include Rotational Deformations" is enabled.

        """

    def GetMinimumSize(self, unit: str | None = None) -> float:
        """
        Get the value of "Minimum Size".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetMinimumSize(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Minimum Size".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetMinimumSizeRatio(self) -> float:
        """
        Get the value of "Minimum Size Ratio".

        """

    def SetMinimumSizeRatio(self, value: str | float) -> None:
        """
        Set the value of "Minimum Size Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetMinimumVolumeFractionForFragmentDisabling(self) -> float:
        """
        Get the value of "Minimum Volume Fraction For Fragment Disabling".

        """

    def SetMinimumVolumeFractionForFragmentDisabling(self, value: str | float) -> None:
        """
        Set the value of "Minimum Volume Fraction For Fragment Disabling".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetTavaresA(self, unit: str | None = None) -> float:
        """
        Get the value of "Tavares A".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "%".
        """

    def SetTavaresA(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Tavares A".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "%".
        """

    def GetTavaresB(self, unit: str | None = None) -> float:
        """
        Get the value of "Tavares B".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetTavaresB(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Tavares B".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetTavaresD0(self, unit: str | None = None) -> float:
        """
        Get the value of "Tavares D0".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetTavaresD0(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Tavares D0".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetTavaresEInf(self, unit: str | None = None) -> float:
        """
        Get the value of "Tavares E Inf".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "J/kg".
        """

    def SetTavaresEInf(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Tavares E Inf".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "J/kg".
        """

    def GetTavaresGamma(self, unit: str | None = None) -> float:
        """
        Get the value of "Tavares Gamma".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetTavaresGamma(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Tavares Gamma".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetTavaresMinimumEnergy(self, unit: str | None = None) -> float:
        """
        Get the value of "Tavares Minimum Energy".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "J/kg".
        """

    def SetTavaresMinimumEnergy(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Tavares Minimum Energy".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "J/kg".
        """

    def GetTavaresPhi(self, unit: str | None = None) -> float:
        """
        Get the value of "Tavares Phi".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetTavaresPhi(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Tavares Phi".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetTavaresRatioEmax(self, unit: str | None = None) -> float:
        """
        Get the value of "Tavares Ratio Emax".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetTavaresRatioEmax(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Tavares Ratio Emax".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetRatioEnergyAfterBreakage(self, unit: str | None = None) -> float:
        """
        Get the value of "Ratio Energy After Breakage".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetRatioEnergyAfterBreakage(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Ratio Energy After Breakage".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetTavaresSigmaSquared(self, unit: str | None = None) -> float:
        """
        Get the value of "Tavares Sigma Squared".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetTavaresSigmaSquared(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Tavares Sigma Squared".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetT10Formula(self) -> str:
        """
        Get "T10 Formula" as a string.

        :return:
            The returned value will be one of [\'it10E_50b\', \'it10E_fract\'].
        """

    def SetT10Formula(self, value: str) -> None:
        """
        Set the value of "T10 Formula".

        :param value:
            The value to set. Must be one of [\'it10E_50b\', \'it10E_fract\'].
        :raises RockyApiError:
            If `value` is not a valid "T10 Formula" option.
        """

    def GetValidT10FormulaValues(self) -> list[str]:
        """
        Get a list of all possible values for "T10 Formula".

        :return:
            The returned list is [\'it10E_50b\', \'it10E_fract\'].
        """

    def GetShearStressLimit(self, unit: str | None = None) -> float:
        """
        Get the value of "Shear Stress Limit".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "N/m2".
        """

    def SetShearStressLimit(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Shear Stress Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "N/m2".
        """

    def GetTensileStressLimit(self, unit: str | None = None) -> float:
        """
        Get the value of "Tensile Stress Limit".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "N/m2".
        """

    def SetTensileStressLimit(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Tensile Stress Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "N/m2".
        """

    def GetEnableBreakage(self) -> bool:
        """
        Get the value of "Enable Breakage".

        """

    def SetEnableBreakage(self, value: bool) -> None:
        """
        Set the value of "Enable Breakage".

        :param value:
            The value to set.
        """

    def EnableBreakage(self) -> None:
        """
        Set the value of "Breakage" to True.
        """

    def DisableBreakage(self) -> None:
        """
        Set the value of "Breakage" to False.
        """

    def IsBreakageEnabled(self) -> bool:
        """
        Check if the "Breakage" is enabled.

        """

    def GetVonMisesStressLimit(self, unit: str | None = None) -> float:
        """
        Get the value of "Von Mises Stress Limit".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "N/m2".
        """

    def SetVonMisesStressLimit(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Von Mises Stress Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "N/m2".
        """

    def GetAllowSelfContacts(self) -> bool:
        """
        Get the value of "Allow Self Contacts".

        """

    def SetAllowSelfContacts(self, value: bool) -> None:
        """
        Set the value of "Allow Self Contacts".

        :param value:
            The value to set.
        """

    def GetDeformationModel(self) -> str:
        """
        Get "Deformation Model" as a string.

        :return:
            The returned value will be one of [\'none\', \'elastic\', \'plastic\'].
        """

    def SetDeformationModel(self, value: str) -> None:
        """
        Set the value of "Deformation Model".

        :param value:
            The value to set. Must be one of [\'none\', \'elastic\', \'plastic\'].
        :raises RockyApiError:
            If `value` is not a valid "Deformation Model" option.
        """

    def GetValidDeformationModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Deformation Model".

        :return:
            The returned list is [\'none\', \'elastic\', \'plastic\'].
        """

    def GetInternalFriction(self) -> float:
        """
        Get the value of "Internal Friction".

        """

    def SetInternalFriction(self, value: str | float) -> None:
        """
        Set the value of "Internal Friction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetPlasticLimit(self, unit: str | None = None) -> float:
        """
        Get the value of "Plastic Limit".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "Pa".
        """

    def SetPlasticLimit(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Plastic Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "Pa".
        """

    def GetFlexible(self) -> bool:
        """
        Get the value of "Flexible".

        """

    def SetFlexible(self, value: bool) -> None:
        """
        Set the value of "Flexible".

        :param value:
            The value to set.
        """

    def GetCenterOfMassOffset(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Center of Mass Offset".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "%".
        """

    def SetCenterOfMassOffset(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Center of Mass Offset".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "%".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetChangeMassProperties(self) -> bool:
        """
        Get the value of "Change Mass Properties".

        """

    def SetChangeMassProperties(self, value: bool) -> None:
        """
        Set the value of "Change Mass Properties".

        :param value:
            The value to set.
        """

    def GetEnableRotations(self) -> bool:
        """
        Get the value of "Enable Rotations".

        """

    def SetEnableRotations(self, value: bool) -> None:
        """
        Set the value of "Enable Rotations".

        :param value:
            The value to set.
        """

    def GetHorizontalAspectRatio(self) -> float:
        """
        Get the value of "Horizontal Aspect Ratio".

        """

    def SetHorizontalAspectRatio(self, value: str | float) -> None:
        """
        Set the value of "Horizontal Aspect Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
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

    def GetNumberOfCorners(self) -> int:
        """
        Get the value of "Number of Corners".

        """

    def SetNumberOfCorners(self, value: str | int) -> None:
        """
        Set the value of "Number of Corners".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetXDirection(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "X Direction".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "-".
        """

    def SetXDirection(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "X Direction".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "-".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetYDirection(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Y Direction".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "-".
        """

    def SetYDirection(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Y Direction".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "-".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetZDirection(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Z Direction".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "-".
        """

    def SetZDirection(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Z Direction".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "-".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetRollingResistance(self) -> float:
        """
        Get the value of "Rolling Resistance".

        """

    def SetRollingResistance(self, value: str | float) -> None:
        """
        Set the value of "Rolling Resistance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSideAngle(self) -> float:
        """
        Get the value of "Side Angle".

        """

    def SetSideAngle(self, value: str | float) -> None:
        """
        Set the value of "Side Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSmoothness(self) -> float:
        """
        Get the value of "Smoothness".

        """

    def SetSmoothness(self, value: str | float) -> None:
        """
        Set the value of "Smoothness".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSuperquadricDegree(self) -> float:
        """
        Get the value of "Superquadric Degree".

        """

    def SetSuperquadricDegree(self, value: str | float) -> None:
        """
        Set the value of "Superquadric Degree".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetThickness(self, unit: str | None = None) -> float:
        """
        Get the value of "Thickness".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetThickness(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Thickness".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetVerticalAspectRatio(self) -> float:
        """
        Get the value of "Vertical Aspect Ratio".

        """

    def SetVerticalAspectRatio(self, value: str | float) -> None:
        """
        Set the value of "Vertical Aspect Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetBendingAngleLimit(self, unit: str | None = None) -> float:
        """
        Get the value of "Bending Angle Limit".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetBendingAngleLimit(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Bending Angle Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
        """

    def GetWithFailure(self) -> bool:
        """
        Get the value of "With Failure".

        """

    def SetWithFailure(self, value: bool) -> None:
        """
        Set the value of "With Failure".

        :param value:
            The value to set.
        """

    def GetEdgeAngle(self, unit: str | None = None) -> float:
        """
        Get the value of "Edge Angle".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetEdgeAngle(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Edge Angle".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
        """

    def GetElasticRatioBending(self) -> float:
        """
        Get the value of "Elastic Ratio Bending".

        """

    def SetElasticRatioBending(self, value: str | float) -> None:
        """
        Set the value of "Elastic Ratio Bending".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetElasticRatioNormal(self) -> float:
        """
        Get the value of "Elastic Ratio Normal".

        """

    def SetElasticRatioNormal(self, value: str | float) -> None:
        """
        Set the value of "Elastic Ratio Normal".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetElasticRatioTangential(self) -> float:
        """
        Get the value of "Elastic Ratio Tangential".

        """

    def SetElasticRatioTangential(self, value: str | float) -> None:
        """
        Set the value of "Elastic Ratio Tangential".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetElasticRatioTorsion(self) -> float:
        """
        Get the value of "Elastic Ratio Torsion".

        """

    def SetElasticRatioTorsion(self, value: str | float) -> None:
        """
        Set the value of "Elastic Ratio Torsion".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetElasticity(self) -> str:
        """
        Get "Elasticity" as a string.

        :return:
            The returned value will be one of [\'isotropic\', \'anisotropic\'].
        """

    def SetElasticity(self, value: str) -> None:
        """
        Set the value of "Elasticity".

        :param value:
            The value to set. Must be one of [\'isotropic\', \'anisotropic\'].
        :raises RockyApiError:
            If `value` is not a valid "Elasticity" option.
        """

    def GetValidElasticityValues(self) -> list[str]:
        """
        Get a list of all possible values for "Elasticity".

        :return:
            The returned list is [\'isotropic\', \'anisotropic\'].
        """

    def GetTargetNumberOfElements(self) -> int:
        """
        Get the value of "Target Number of Elements".

        """

    def SetTargetNumberOfElements(self, value: str | int) -> None:
        """
        Set the value of "Target Number of Elements".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetElementDampingRatio(self) -> float:
        """
        Get the value of "Element Damping Ratio".

        """

    def SetElementDampingRatio(self, value: str | float) -> None:
        """
        Set the value of "Element Damping Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetFailureRatio(self) -> float:
        """
        Get the value of "Failure Ratio".

        """

    def SetFailureRatio(self, value: str | float) -> None:
        """
        Set the value of "Failure Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetJointDampingRatio(self) -> float:
        """
        Get the value of "Joint Damping Ratio".

        """

    def SetJointDampingRatio(self, value: str | float) -> None:
        """
        Set the value of "Joint Damping Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetJointElasticRatio(self) -> float:
        """
        Get the value of "Joint Elastic Ratio".

        """

    def SetJointElasticRatio(self, value: str | float) -> None:
        """
        Set the value of "Joint Elastic Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetJointThermalRatio(self) -> float:
        """
        Get the value of "Joint Thermal Ratio".

        """

    def SetJointThermalRatio(self, value: str | float) -> None:
        """
        Set the value of "Joint Thermal Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetPlasticRatio(self) -> float:
        """
        Get the value of "Plastic Ratio".

        """

    def SetPlasticRatio(self, value: str | float) -> None:
        """
        Set the value of "Plastic Ratio".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetPlasticityModel(self) -> str:
        """
        Get "Plasticity Model" as a string.

        :return:
            The returned value will be one of [\'LinearElastic\', \'BilinearElastoplastic\', \'Custom\'].
        """

    def SetPlasticityModel(self, value: str) -> None:
        """
        Set the value of "Plasticity Model".

        :param value:
            The value to set. Must be one of [\'LinearElastic\', \'BilinearElastoplastic\', \'Custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Plasticity Model" option.
        """

    def GetValidPlasticityModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Plasticity Model".

        :return:
            The returned list is [\'LinearElastic\', \'BilinearElastoplastic\', \'Custom\'].
        """

    def GetRemeshToTarget(self) -> bool:
        """
        Get the value of "Remesh To Target".

        """

    def SetRemeshToTarget(self, value: bool) -> None:
        """
        Set the value of "Remesh To Target".

        :param value:
            The value to set.
        """

    def GetSecondBendingAngleLimit(self, unit: str | None = None) -> float:
        """
        Get the value of "Second Bending Angle Limit".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetSecondBendingAngleLimit(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Second Bending Angle Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
        """

    def GetTorsionAngleLimit(self, unit: str | None = None) -> float:
        """
        Get the value of "Torsion Angle Limit".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "dega".
        """

    def SetTorsionAngleLimit(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Torsion Angle Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "dega".
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

    def GetRandomAnglesHalfRange(self, unit: str | None = None) -> list[float]:
        """
        Get the value of "Random Angles Half Range".

        :param unit:
            The unit for the returned values. If no unit is provided, the returned values will be in "rad".
        """

    def SetRandomAnglesHalfRange(
        self, values: Sequence[str | float], unit: str | None = None
    ) -> None:
        """
        Set the values of "Random Angles Half Range".

        :param values:
            The values to set. The values can be heterogeneous, the element of values can be an
            expression with input variables or a float. Must have exactly 3 elements.
        :param unit:
            The unit for `values`. If no unit is provided, `values` is assumed to be in "rad".
        :raises RockyApiError:
            If `values` doesn\'t have exactly 3 elements.
        """

    def GetShape(self) -> str:
        """
        Get "Shape" as a string.

        :return:
            The returned value will be one of [\'sphere\', \'polyhedron\', \'sphero_cylinder\', \'sphero_polygon\', \'sphero_polyhedron\', \'briquete\', \'faceted_cylinder\', \'assembly\', \'straight_fiber\', \'custom_fiber\', \'custom_shell\', \'custom_polyhedron\'].
        """

    def SetShape(self, value: str) -> None:
        """
        Set the value of "Shape".

        :param value:
            The value to set. Must be one of [\'sphere\', \'polyhedron\', \'sphero_cylinder\', \'sphero_polygon\', \'sphero_polyhedron\', \'briquete\', \'faceted_cylinder\', \'assembly\', \'straight_fiber\', \'custom_fiber\', \'custom_shell\', \'custom_polyhedron\'].
        :raises RockyApiError:
            If `value` is not a valid "Shape" option.
        """

    def GetValidShapeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Shape".

        :return:
            The returned list is [\'sphere\', \'polyhedron\', \'sphero_cylinder\', \'sphero_polygon\', \'sphero_polyhedron\', \'briquete\', \'faceted_cylinder\', \'assembly\', \'straight_fiber\', \'custom_fiber\', \'custom_shell\', \'custom_polyhedron\'].
        """

    def GetCgmScaleFactor(self) -> float:
        """
        Get the value of "Cgm Scale Factor".

        """

    def SetCgmScaleFactor(self, value: str | float) -> None:
        """
        Set the value of "Cgm Scale Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSizeType(self) -> str:
        """
        Get "Size Type" as a string.

        :return:
            The returned value will be one of [\'sieve\', \'equivalent_diameter\', \'original_size_scale\'].
        """

    def SetSizeType(self, value: str) -> None:
        """
        Set the value of "Size Type".

        :param value:
            The value to set. Must be one of [\'sieve\', \'equivalent_diameter\', \'original_size_scale\'].
        :raises RockyApiError:
            If `value` is not a valid "Size Type" option.
        """

    def GetValidSizeTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Size Type".

        :return:
            The returned list is [\'sieve\', \'equivalent_diameter\', \'original_size_scale\'].
        """

    def GetEnableRandomAngle(self) -> bool:
        """
        Get the value of "Enable Random Angle".

        """

    def SetEnableRandomAngle(self, value: bool) -> None:
        """
        Set the value of "Enable Random Angle".

        :param value:
            The value to set.
        """

    def EnableRandomOrientation(self) -> None:
        """
        Set the value of "Random Orientation" to True.
        """

    def DisableRandomOrientation(self) -> None:
        """
        Set the value of "Random Orientation" to False.
        """

    def IsRandomOrientationEnabled(self) -> bool:
        """
        Check if the "Random Orientation" is enabled.

        """

    def GetMaterial(self):
        """
        Get the "Material".

        :rtype: :class:`RASolidMaterial`
        """

    def SetMaterial(self, value) -> None:
        """
        Set the "Material".

        :param unicode, :class:`RASolidMaterial` value:
            Either the API object wrapping the desired entity or its name.
        """

    def GetAvailableMaterials(self):
        """
        Get all available Materials.

        :rtype: List[:class:`RASolidMaterial`]
            A list of :class:`RASolidMaterial`.
        """

    def GetAnisotropic(self) -> bool:
        """
        Deprecated: Use :meth:`GetElasticity()` instead.

        :rtype: bool
        """

    def SetAnisotropic(self, value: bool) -> None:
        """
        Set the value of "Anisotropic".

        :param bool value:
            The value to set.
        """
    GetPrincipalMomentOfInertia: Incomplete
    SetPrincipalMomentOfInertia: Incomplete
    GetXDirection: Incomplete
    SetXDirection: Incomplete
    GetYDirection: Incomplete
    SetYDirection: Incomplete
    GetZDirection: Incomplete
    SetZDirection: Incomplete
    GetPorosity: Incomplete
    SetPorosity: Incomplete
