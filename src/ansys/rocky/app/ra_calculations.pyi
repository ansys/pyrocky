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

from collections.abc import Iterator

from rocky30.models.rocky_model_type import MatchModelType as MatchModelType
from rocky30.models.rocky_model_type import RockyModelTypeEnum as RockyModelTypeEnum
from rocky30.plugins.particles_calculations.particles_calculations import (
    ParticlesCalculations as ParticlesCalculations,
)
from rocky30.plugins.particles_calculations.particles_selection_calculator import (
    ParticlesSelectionCalculator as ParticlesSelectionCalculator,
)
from rocky30.plugins.particles_calculations.relative_velocity.relative_velocity_command import (
    FrameBasedRelativeVelocityCommand as FrameBasedRelativeVelocityCommand,
)
from rocky30.plugins.particles_calculations.selection_flip_count_calculation import (
    ParticlesSelectionFlipCountCommand as ParticlesSelectionFlipCountCommand,
)
from rocky30.plugins.particles_calculations.selection_residence_time_calculation import (
    BaseParticleResidenceTimeCalculator as BaseParticleResidenceTimeCalculator,
)
from rocky30.plugins.particles_calculations.selection_residence_time_calculation import (
    ParticlesSelectionResidenceTimeCommand as ParticlesSelectionResidenceTimeCommand,
)
from rocky30.plugins.particles_calculations.tagging.calculator.divisions_tagging_calculator import (
    DivisionsTaggingCalculator as DivisionsTaggingCalculator,
)
from rocky30.plugins.particles_calculations.tagging.calculator.particle_tagging_calculator import (
    ParticleTaggingCalculator as ParticleTaggingCalculator,
)
from rocky30.plugins.particles_calculations.tagging.tagging_command import (
    DivisionsTaggingCommand as DivisionsTaggingCommand,
)
from rocky30.plugins.particles_calculations.tagging.tagging_command import (
    ParticleTaggingCommand as ParticleTaggingCommand,
)
from rocky30.plugins.sph.calculations.residence_time.sph_selection_residence_time_command import (
    SphSelectionResidenceTimeCommand as SphSelectionResidenceTimeCommand,
)
from rocky30.plugins.sph.calculations.tagging.sph_tagging_calculator import (
    SPHTaggingCalculator as SPHTaggingCalculator,
)
from rocky30.plugins.sph.calculations.tagging.sph_tagging_command import (
    SPHTaggingCommand as SPHTaggingCommand,
)

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_api import RockyApiError as RockyApiError
from ansys.rocky.app.ra_divisions_tagging import RADivisionsTagging as RADivisionsTagging
from ansys.rocky.app.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)
from ansys.rocky.app.ra_relative_velocity_calculator import (
    RARelativeVelocityCalculator as RARelativeVelocityCalculator,
)
from ansys.rocky.app.ra_residence_time import RAResidenceTime as RAResidenceTime
from ansys.rocky.app.ra_sph_residence_time import RASPHResidenceTime as RASPHResidenceTime
from ansys.rocky.app.ra_sph_tagging import RASPHTagging as RASPHTagging
from ansys.rocky.app.ra_tagging import RATagging as RATagging

class RACalculations(ApiElementItem):
    """
    Rocky api for particles calculations
    """

    @classmethod
    def GetWrappedClass(self) -> type[ParticlesCalculations]: ...
    @classmethod
    def GetClassName(self) -> str: ...
    def CreateSelectionResidenceTime(
        self, selection: RAGridProcessElementItem | str
    ) -> RAResidenceTime | RASPHResidenceTime:
        """
        Create a residence time grid function for the given selection process
        """

    def CreateSelectionFlipCount(
        self, selection: RAGridProcessElementItem
    ) -> ParticlesSelectionCalculator:
        """
        Create a flip count grid function for the given selection process
        """

    def CreateFrameBasedResultsCalculator(
        self, selection: RAGridProcessElementItem
    ) -> RARelativeVelocityCalculator:
        """
        Create a Frame-Based Results calculator for the given selection process
        """

    def GetTagging(self, name: str) -> RATagging:
        """
        Get the Tagging calculator with the given name.
        """

    def GetDivisionsTagging(self, name: str) -> RADivisionsTagging:
        """
        Get the Divisions Tagging calculator with the given name.
        """

    def GetTaggingNames(self) -> list[str]:
        """
        Get a list of the names of all Taggings in Calculations.
        """

    def GetDivisionsTaggingNames(self) -> list[str]:
        """
        Get a list of the names of all Divisions Taggings in Particles Calculations.
        """

    def GetResidenceTimeNames(self) -> list[str]:
        """
        Get a list of the names of all Residence Time calculators in Calculations.
        """

    def CreateTagging(
        self, selection: RAGridProcessElementItem
    ) -> ParticlesSelectionCalculator | None:
        """
        Create a Tagging calculator for the given particle-based selection process.

        :param selection:
            Must be a particle selection type.
        """

    def CreateDivisionsTagging(
        self, selection: RAGridProcessElementItem
    ) -> RADivisionsTagging:
        """
        Create a Divisions Tagging calculator for the given particle-based selection process.

        :param selection:
            Must be a particle selection type.
        """

    def __iter__(self) -> Iterator:
        """
        Iterates over the wrapped particle calculations.
        """

    def __len__(self) -> int:
        """
        :rtype: int
        :return:
            The number of particle calculations
        """

    def __getitem__(self, index: int) -> ParticlesSelectionCalculator:
        """
        :param index:
            The calculation index

        :return:
            The particle calculation at the given index
        """
