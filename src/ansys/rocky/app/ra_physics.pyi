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

class RAPhysics(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper to manipulate physics properties.

    This class represents the "Physics" item on the project data tree. To get the :class:`RAPhysics`
    from a :class:`RAStudy`, use:

    .. code-block:: python

        physics = study.GetPhysics()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    @property
    def enable_thermal_model(self): ...
    def GetAdhesionModel(self) -> str:
        """
        Get "Adhesion Model" as a string.

        :return:
            The returned value will be one of [\'none\', \'constant\', \'linear\', \'JKR\', \'custom\'].
        """

    def SetAdhesionModel(self, value: str) -> None:
        """
        Set the value of "Adhesion Model".

        :param value:
            The value to set. Must be one of [\'none\', \'constant\', \'linear\', \'JKR\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Adhesion Model" option.
        """

    def GetValidAdhesionModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Adhesion Model".

        :return:
            The returned list is [\'none\', \'constant\', \'linear\', \'JKR\', \'custom\'].
        """

    def GetClosePackingVolumeFraction(self) -> float:
        """
        Get the value of "Close Packing Volume Fraction".

        """

    def SetClosePackingVolumeFraction(self, value: str | float) -> None:
        """
        Set the value of "Close Packing Volume Fraction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetEnableCoarseGrainModeling(self) -> bool:
        """
        Get the value of "Enable Coarse Grain Modeling".

        """

    def SetEnableCoarseGrainModeling(self, value: bool) -> None:
        """
        Set the value of "Enable Coarse Grain Modeling".

        :param value:
            The value to set.
        """

    def GetEnableThermalModel(self) -> bool:
        """
        Get the value of "Enable Thermal Model".

        """

    def SetEnableThermalModel(self, value: bool) -> None:
        """
        Set the value of "Enable Thermal Model".

        :param value:
            The value to set.
        """

    def GetGravityStartTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Gravity Start Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetGravityStartTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Gravity Start Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetGravityStopTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Gravity Stop Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetGravityStopTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Gravity Stop Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetGravityXDirection(self, unit: str | None = None) -> float:
        """
        Get the value of "Gravity X Direction".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s2".
        """

    def SetGravityXDirection(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Gravity X Direction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s2".
        """

    def GetGravityYDirection(self, unit: str | None = None) -> float:
        """
        Get the value of "Gravity Y Direction".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s2".
        """

    def SetGravityYDirection(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Gravity Y Direction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s2".
        """

    def GetGravityZDirection(self, unit: str | None = None) -> float:
        """
        Get the value of "Gravity Z Direction".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m/s2".
        """

    def SetGravityZDirection(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Gravity Z Direction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m/s2".
        """

    def GetImpactEnergyModel(self) -> str:
        """
        Get "Impact Energy Model" as a string.

        :return:
            The returned value will be one of [\'default\', \'custom\'].
        """

    def SetImpactEnergyModel(self, value: str) -> None:
        """
        Set the value of "Impact Energy Model".

        :param value:
            The value to set. Must be one of [\'default\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Impact Energy Model" option.
        """

    def GetValidImpactEnergyModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Impact Energy Model".

        :return:
            The returned list is [\'default\', \'custom\'].
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

    def GetNormalForceModel(self) -> str:
        """
        Get "Normal Force Model" as a string.

        :return:
            The returned value will be one of [\'linear_hysteresis\', \'linear_elastic_viscous\', \'damped_hertzian\', \'custom\'].
        """

    def SetNormalForceModel(self, value: str) -> None:
        """
        Set the value of "Normal Force Model".

        :param value:
            The value to set. Must be one of [\'linear_hysteresis\', \'linear_elastic_viscous\', \'damped_hertzian\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Normal Force Model" option.
        """

    def GetValidNormalForceModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Normal Force Model".

        :return:
            The returned list is [\'linear_hysteresis\', \'linear_elastic_viscous\', \'damped_hertzian\', \'custom\'].
        """

    def GetRollingResistanceModel(self) -> str:
        """
        Get "Rolling Resistance Model" as a string.

        :return:
            The returned value will be one of [\'type_1\', \'type_3\', \'none\', \'custom\'].
        """

    def SetRollingResistanceModel(self, value: str) -> None:
        """
        Set the value of "Rolling Resistance Model".

        :param value:
            The value to set. Must be one of [\'type_1\', \'type_3\', \'none\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Rolling Resistance Model" option.
        """

    def GetValidRollingResistanceModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Rolling Resistance Model".

        :return:
            The returned list is [\'type_1\', \'type_3\', \'none\', \'custom\'].
        """

    def GetExponentLimit(self) -> float:
        """
        Get the value of "Exponent Limit".

        """

    def SetExponentLimit(self, value: str | float) -> None:
        """
        Set the value of "Exponent Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetVolumeFractionLimit(self) -> float:
        """
        Get the value of "Volume Fraction Limit".

        """

    def SetVolumeFractionLimit(self, value: str | float) -> None:
        """
        Set the value of "Volume Fraction Limit".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetRestitutionModel(self) -> str:
        """
        Get "Restitution Model" as a string.

        :return:
            The returned value will be one of [\'constant\', \'velocity_dependent\'].
        """

    def SetRestitutionModel(self, value: str) -> None:
        """
        Set the value of "Restitution Model".

        :param value:
            The value to set. Must be one of [\'constant\', \'velocity_dependent\'].
        :raises RockyApiError:
            If `value` is not a valid "Restitution Model" option.
        """

    def GetValidRestitutionModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Restitution Model".

        :return:
            The returned list is [\'constant\', \'velocity_dependent\'].
        """

    def GetSearchDistanceMultiplier(self) -> float:
        """
        Get the value of "Search Distance Multiplier".

        """

    def SetSearchDistanceMultiplier(self, value: str | float) -> None:
        """
        Set the value of "Search Distance Multiplier".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetSphThermalTransferModel(self) -> str:
        """
        Get "Sph Thermal Transfer Model" as a string.

        :return:
            The returned value will be one of [\'cleary\', \'custom\'].
        """

    def SetSphThermalTransferModel(self, value: str) -> None:
        """
        Set the value of "Sph Thermal Transfer Model".

        :param value:
            The value to set. Must be one of [\'cleary\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Sph Thermal Transfer Model" option.
        """

    def GetValidSphThermalTransferModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Sph Thermal Transfer Model".

        :return:
            The returned list is [\'cleary\', \'custom\'].
        """

    def GetNumericalSofteningFactor(self) -> float:
        """
        Get the value of "Numerical Softening Factor".

        """

    def SetNumericalSofteningFactor(self, value: str | float) -> None:
        """
        Set the value of "Numerical Softening Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetTangentialForceModel(self) -> str:
        """
        Get "Tangential Force Model" as a string.

        :return:
            The returned value will be one of [\'elastic_coulomb\', \'coulomb_limit\', \'mindlin_deresiewicz\', \'custom\'].
        """

    def SetTangentialForceModel(self, value: str) -> None:
        """
        Set the value of "Tangential Force Model".

        :param value:
            The value to set. Must be one of [\'elastic_coulomb\', \'coulomb_limit\', \'mindlin_deresiewicz\', \'custom\'].
        :raises RockyApiError:
            If `value` is not a valid "Tangential Force Model" option.
        """

    def GetValidTangentialForceModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Tangential Force Model".

        :return:
            The returned list is [\'elastic_coulomb\', \'coulomb_limit\', \'mindlin_deresiewicz\', \'custom\'].
        """

    def GetThermalCorrectionModel(self) -> str:
        """
        Get "Thermal Correction Model" as a string.

        :return:
            The returned value will be one of [\'none\', \'morris_et_al_area\', \'morris_et_al_area_time\'].
        """

    def SetThermalCorrectionModel(self, value: str) -> None:
        """
        Set the value of "Thermal Correction Model".

        :param value:
            The value to set. Must be one of [\'none\', \'morris_et_al_area\', \'morris_et_al_area_time\'].
        :raises RockyApiError:
            If `value` is not a valid "Thermal Correction Model" option.
        """

    def GetValidThermalCorrectionModelValues(self) -> list[str]:
        """
        Get a list of all possible values for "Thermal Correction Model".

        :return:
            The returned list is [\'none\', \'morris_et_al_area\', \'morris_et_al_area_time\'].
        """

    def GetUpdateDistanceMultiplier(self) -> float:
        """
        Get the value of "Update Distance Multiplier".

        """

    def SetUpdateDistanceMultiplier(self, value: str | float) -> None:
        """
        Set the value of "Update Distance Multiplier".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetUseRadlEtAl(self) -> bool:
        """
        Get the value of "Use Radl Et Al".

        """

    def SetUseRadlEtAl(self, value: bool) -> None:
        """
        Set the value of "Use Radl Et Al".

        :param value:
            The value to set.
        """
