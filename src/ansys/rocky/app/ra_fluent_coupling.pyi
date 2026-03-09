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

from collections.abc import Iterable

from _typeshed import Incomplete

from ansys.rocky.app.ra_api import RockyApiError as RockyApiError
from ansys.rocky.app.ra_cfd_coupling import RABaseCFDCoupling as RABaseCFDCoupling

class RAFluentOneWayCoupling(RABaseCFDCoupling):
    """
    Rocky PrePost Scripting wrapper to Fluent one way CFD coupling process.

    This wrapper can be accessed via the project's :class:`RACFDCoupling`:

    .. code-block:: python

        cfd_coupling = study.GetCFDCoupling()
        cfd_coupling.SetupOneWayFluent('fluent.cas')
        one_way_process = cfd_coupling.GetCouplingProcess()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def SetupStoreFiles(self, filename) -> None:
        """
        Set the file with Fluent to Rocky information.

        :param str filename:
            The filename for the .f2r file.
        """

    def GetAvailableCoupledBoundaryNames(self) -> Iterable[str]:
        """
        Obtain the names of the boundaries available for coupling in the fluent file.
        """

    def CreateCoupledBoundaries(self, coupled_boundary_names: list[str]) -> None:
        """
        Create a coupled boundary for each of the coupled boundary name passed by the user.
        Check GetAvailableCoupledBoundaryNames to obtain the list of available boundaries.
        """

    def GetIsOneWayPeriodic(self) -> bool:
        """
        Get the value of "Is One Way Periodic".

        """

    def SetIsOneWayPeriodic(self, value: bool) -> None:
        """
        Set the value of "Is One Way Periodic".

        :param value:
            The value to set.
        """

    def GetOverwriteCfdUpdateDistance(self) -> bool:
        """
        Get the value of "Overwrite Cfd Update Distance".

        """

    def SetOverwriteCfdUpdateDistance(self, value: bool) -> None:
        """
        Set the value of "Overwrite Cfd Update Distance".

        :param value:
            The value to set.
        """

    def GetStartTime(self, unit: str | None = None) -> float:
        """
        Get the value of "Start Time".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "s".
        """

    def SetStartTime(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Start Time".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "s".
        """

    def GetUseTurbulentDispersion(self) -> bool:
        """
        Get the value of "Use Turbulent Dispersion".

        """

    def SetUseTurbulentDispersion(self, value: bool) -> None:
        """
        Set the value of "Use Turbulent Dispersion".

        :param value:
            The value to set.
        """

    def GetUserCfdUpdateDistance(self, unit: str | None = None) -> float:
        """
        Get the value of "User Cfd Update Distance".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetUserCfdUpdateDistance(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "User Cfd Update Distance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

class RAFluentTwoWayCoupling(RABaseCFDCoupling):
    """
    Rocky PrePost Scripting wrapper to manipulate Fluent Two-Way coupling properties.

    This wrapper can be accessed via the project's :class:`RACFDCoupling`:

    .. code-block:: python

        cfd_coupling = study.GetCFDCoupling()
        cfd_coupling.SetupFluentTwoWay('fluent.cas')
        two_way_process = cfd_coupling.GetCouplingProcess()
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def SetPartIdIfValid(self) -> None: ...
    def GetFluentReleases(self):
        """
        Get a list of available Fluent releases.

        :rtype: list(unicode)
        :return: The list of available Fluent releases
        """

    @property
    def fluent_release(self): ...
    @fluent_release.setter
    def fluent_release(self, value) -> None: ...
    @property
    def fluent_phases(self): ...
    @fluent_phases.setter
    def fluent_phases(self, value) -> None: ...
    @property
    def fluent_rocky_phase(self): ...
    @fluent_rocky_phase.setter
    def fluent_rocky_phase(self, value) -> None: ...
    @property
    def fluent_solver_processes(self): ...
    @fluent_solver_processes.setter
    def fluent_solver_processes(self, value) -> None: ...
    @property
    def use_dat_initialization(self): ...
    @use_dat_initialization.setter
    def use_dat_initialization(self, value) -> None: ...
    @property
    def fluent_output_frequency_multiplier(self): ...
    @property
    def coupling_files_kept(self): ...
    @property
    def fluent_time_step(self): ...
    @property
    def additional_input_variables(self): ...
    @property
    def additional_output_variables(self): ...
    @property
    def disabled_input_variables(self): ...
    @disabled_input_variables.setter
    def disabled_input_variables(self, value) -> None: ...
    @property
    def disabled_output_variables(self): ...
    @disabled_output_variables.setter
    def disabled_output_variables(self, values) -> None: ...
    def SetupDatFilename(self, dat_filename): ...
    dat_filename: Incomplete
    cas_filename: Incomplete
    def StartFluent(self) -> None:
        """
        Starts Fluent application
        """

    def IsFluentRunning(self):
        """
        Whether a Rocky-created Fluent process is running.

        :return:
            True whether a Fluent application is running false otherwise
        """

    def CloseFluent(self) -> None:
        """
        Closes a running Fluent application
        """

    def UpdateFluentInfo(self) -> None:
        """
        Updates the latest changes from Fluent setup.
        """

    def SetupStoreFiles(self, cas_filename, case_config=None) -> None:
        """
        Copies CAS file to Rocky's project folder and update Fluent info
        """

    def GetFluentVersion(self):
        """
        Get the value of "Version".

        :rtype: str
        """

    def SetFluentVersion(self, fluent_version) -> None:
        """
        Set the Ansys Fluent version to be used in CFD coupling (deprecated).

        Currently, it's not possible to change the version of Ansys Fluent used for CFD coupling.
        This method is being kept for backward compatibility (and also because there's a chance
        of this feature to be brought back in future version).
        """

    def GetAvailableCoupledBoundaryNames(self) -> Iterable[str]:
        """
        Obtain the names of the boundaries available for coupling in the fluent file.
        """

    def CreateCoupledBoundaries(self, coupled_boundary_names: list[str]) -> None:
        """
        Create a coupled boundary for each of the coupled boundary name passed by the user.
        Check GetAvailableCoupledBoundaryNames to obtain the list of available boundaries.
        """

    def GetAbsoluteValue(self, unit: str | None = None) -> float:
        """
        Get the value of "Absolute Value".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetAbsoluteValue(self, value: str | float, unit: str | None = None) -> None:
        """
        Set the value of "Absolute Value".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """

    def GetMaximumIterations(self) -> int:
        """
        Get the value of "Maximum Iterations".

        """

    def SetMaximumIterations(self, value: str | int) -> None:
        """
        Set the value of "Maximum Iterations".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetMappingMethod(self) -> str:
        """
        Get "Mapping Method" as a string.

        :return:
            The returned value will be one of [\'UniformDistribution\', \'VolumetricDiffusion\', \'DiffusionSolution\'].
        """

    def SetMappingMethod(self, value: str) -> None:
        """
        Set the value of "Mapping Method".

        :param value:
            The value to set. Must be one of [\'UniformDistribution\', \'VolumetricDiffusion\', \'DiffusionSolution\'].
        :raises RockyApiError:
            If `value` is not a valid "Mapping Method" option.
        """

    def GetValidMappingMethodValues(self) -> list[str]:
        """
        Get a list of all possible values for "Mapping Method".

        :return:
            The returned list is [\'UniformDistribution\', \'VolumetricDiffusion\', \'DiffusionSolution\'].
        """

    def GetAveragingMethod(self) -> str:
        """
        Deprecated: Use :meth:`GetMappingMethod()` instead.

        :return:
            The returned value will be one of ['UniformDistribution', 'VolumetricDiffusion', 'DiffusionSolution'].
        """

    def SetAveragingMethod(self, value: str):
        """
        Deprecated: Use :meth:`SetMappingMethod()` instead.

        :param value:
            The value to set. Must be one of [\'UniformDistribution\', \'VolumetricDiffusion\', \'DiffusionSolution\'].
        :raises RockyApiError:
            If `value` is not a valid "Averaging Method" option.
        """

    def GetValidAveragingMethodValues(self) -> list[str]:
        """
        Deprecated: Use :meth:`GetValidMappingMethodValues()` instead.

        :return:
            The returned list is ['UniformDistribution', 'VolumetricDiffusion', 'DiffusionSolution'].
        """

    def GetMinimumIterations(self) -> int:
        """
        Get the value of "Minimum Iterations".

        """

    def SetMinimumIterations(self, value: str | int) -> None:
        """
        Set the value of "Minimum Iterations".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetAveragingRadiusType(self) -> str:
        """
        Get "Averaging Radius Type" as a string.

        :return:
            The returned value will be one of [\'FractionMaximumParticleSize\', \'AbsoluteValue\'].
        """

    def SetAveragingRadiusType(self, value: str) -> None:
        """
        Set the value of "Averaging Radius Type".

        :param value:
            The value to set. Must be one of [\'FractionMaximumParticleSize\', \'AbsoluteValue\'].
        :raises RockyApiError:
            If `value` is not a valid "Averaging Radius Type" option.
        """

    def GetValidAveragingRadiusTypeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Averaging Radius Type".

        :return:
            The returned list is [\'FractionMaximumParticleSize\', \'AbsoluteValue\'].
        """

    def GetSolidsMaximumVolumeFractionTarget(self) -> float:
        """
        Get the value of "Solids Maximum Volume Fraction Target".

        """

    def SetSolidsMaximumVolumeFractionTarget(self, value: str | float) -> None:
        """
        Set the value of "Solids Maximum Volume Fraction Target".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetVolumeFractionTarget(self) -> float:
        """
        Deprecated: Use :meth:`GetSolidsMaximumVolumeFractionTarget()` instead.

        """

    def SetVolumeFractionTarget(self, value: float) -> None:
        """
        Deprecated: Use :meth:`SetSolidsMaximumVolumeFractionTarget()` instead.

        :param value:
            The value to set.
        """

    def GetCouplingFilesKept(self) -> int:
        """
        Get the value of "Coupling Files Kept".

        """

    def SetCouplingFilesKept(self, value: str | int) -> None:
        """
        Set the value of "Coupling Files Kept".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetDecompositionFactor(self) -> float:
        """
        Get the value of "Decomposition Factor".

        """

    def SetDecompositionFactor(self, value: str | float) -> None:
        """
        Set the value of "Decomposition Factor".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetDiffusionCoefficient(self, unit: str | None = None) -> float:
        """
        Get the value of "Diffusion Coefficient".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m2/s".
        """

    def SetDiffusionCoefficient(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Diffusion Coefficient".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m2/s".
        """

    def GetFluentAdditionalArgs(self) -> str:
        """
        Get the value of "Fluent Additional Args".

        """

    def SetFluentAdditionalArgs(self, value: str) -> None:
        """
        Set the value of "Fluent Additional Args".

        :param value:
            The value to set.
        """

    def GetFluentExecutionMode(self) -> str:
        """
        Get "Fluent Execution Mode" as a string.

        :return:
            The returned value will be one of [\'serial\', \'local_parallel\', \'distributed_parallel\'].
        """

    def SetFluentExecutionMode(self, value: str) -> None:
        """
        Set the value of "Fluent Execution Mode".

        :param value:
            The value to set. Must be one of [\'serial\', \'local_parallel\', \'distributed_parallel\'].
        :raises RockyApiError:
            If `value` is not a valid "Fluent Execution Mode" option.
        """

    def GetValidFluentExecutionModeValues(self) -> list[str]:
        """
        Get a list of all possible values for "Fluent Execution Mode".

        :return:
            The returned list is [\'serial\', \'local_parallel\', \'distributed_parallel\'].
        """

    def GetFluentOutputFrequencyMultiplier(self) -> int:
        """
        Get the value of "Fluent Output Frequency Multiplier".

        """

    def SetFluentOutputFrequencyMultiplier(self, value: str | int) -> None:
        """
        Set the value of "Fluent Output Frequency Multiplier".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetFluentSolverProcesses(self) -> int:
        """
        Get the value of "Fluent Solver Processes".

        """

    def SetFluentSolverProcesses(self, value: str | int) -> None:
        """
        Set the value of "Fluent Solver Processes".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetFractionParticleSize(self, unit: str | None = None) -> float:
        """
        Get the value of "Fraction Particle Size".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetFractionParticleSize(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Fraction Particle Size".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetMaximumResidualTolerance(self) -> float:
        """
        Get the value of "Maximum Residual Tolerance".

        """

    def SetMaximumResidualTolerance(self, value: str | float) -> None:
        """
        Set the value of "Maximum Residual Tolerance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        """

    def GetMaximumTimeSteps(self) -> int:
        """
        Get the value of "Maximum Time Steps".

        """

    def SetMaximumTimeSteps(self, value: str | int) -> None:
        """
        Set the value of "Maximum Time Steps".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetMinimumTimeSteps(self) -> int:
        """
        Get the value of "Minimum Time Steps".

        """

    def SetMinimumTimeSteps(self, value: str | int) -> None:
        """
        Set the value of "Minimum Time Steps".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetNumberOfSubsteps(self) -> int:
        """
        Get the value of "Number of Substeps".

        """

    def SetNumberOfSubsteps(self, value: str | int) -> None:
        """
        Set the value of "Number of Substeps".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetNumberOfThreads(self) -> int:
        """
        Get the value of "Number of Threads".

        """

    def SetNumberOfThreads(self, value: str | int) -> None:
        """
        Set the value of "Number of Threads".

        :param value:
            The value to set. This value can be an expression with input variables or int type.
        """

    def GetOverwriteCfdUpdateDistance(self) -> bool:
        """
        Get the value of "Overwrite Cfd Update Distance".

        """

    def SetOverwriteCfdUpdateDistance(self, value: bool) -> None:
        """
        Set the value of "Overwrite Cfd Update Distance".

        :param value:
            The value to set.
        """

    def GetMaximumVolumeFraction(self, unit: str | None = None) -> float:
        """
        Get the value of "Maximum Volume Fraction".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "-".
        """

    def SetMaximumVolumeFraction(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "Maximum Volume Fraction".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "-".
        """

    def GetBackDiffusion(self) -> bool:
        """
        Get the value of "Back Diffusion".

        """

    def SetBackDiffusion(self, value: bool) -> None:
        """
        Set the value of "Back Diffusion".

        :param value:
            The value to set.
        """

    def EnableBackDiffusion(self) -> None:
        """
        Set the value of "Back Diffusion" to True.
        """

    def DisableBackDiffusion(self) -> None:
        """
        Set the value of "Back Diffusion" to False.
        """

    def IsBackDiffusionEnabled(self) -> bool:
        """
        Check if the "Back Diffusion" is enabled.

        """

    def GetUseDatInitialization(self) -> bool:
        """
        Get the value of "Use Dat Initialization".

        """

    def SetUseDatInitialization(self, value: bool) -> None:
        """
        Set the value of "Use Dat Initialization".

        :param value:
            The value to set.
        """

    def GetSubstepping(self) -> bool:
        """
        Get the value of "Substepping".

        """

    def SetSubstepping(self, value: bool) -> None:
        """
        Set the value of "Substepping".

        :param value:
            The value to set.
        """

    def EnableSubstepping(self) -> None:
        """
        Set the value of "Substepping" to True.
        """

    def DisableSubstepping(self) -> None:
        """
        Set the value of "Substepping" to False.
        """

    def IsSubsteppingEnabled(self) -> bool:
        """
        Check if the "Substepping" is enabled.

        """

    def GetUseTurbulentDispersion(self) -> bool:
        """
        Get the value of "Use Turbulent Dispersion".

        """

    def SetUseTurbulentDispersion(self, value: bool) -> None:
        """
        Set the value of "Use Turbulent Dispersion".

        :param value:
            The value to set.
        """

    def GetUserCfdUpdateDistance(self, unit: str | None = None) -> float:
        """
        Get the value of "User Cfd Update Distance".

        :param unit:
            The unit for the returned value. If no unit is provided, the returned value will be in "m".
        """

    def SetUserCfdUpdateDistance(
        self, value: str | float, unit: str | None = None
    ) -> None:
        """
        Set the value of "User Cfd Update Distance".

        :param value:
            The value to set. This value can be an expression with input variables or float type.
        :param unit:
            The unit for `value`. If no unit is provided, `value` is assumed to be in "m".
        """
