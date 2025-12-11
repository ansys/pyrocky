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

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_particle import (
    RAParticle as RAParticle,
)

class RAParticleCollection(RAList[RAParticle]):
    """
    Rocky PrePost Scripting wrapper for the collection of particles in a project.

    This wrapper corresponds to the "Particles" item in the project\'s data tree. To retrieve the
    :class:`RAParticleCollection` from a :class:`RAStudy`, use:

    .. code-block:: python

        particle_collection = study.GetParticleCollection()

    Instances of the :class:`RAParticleCollection` class act as regular Python lists, and can be
    iterated on, accessed via index, etc:

    .. code-block:: python

        particle_1 = particle_collection.New()
        particle_2 = particle_collection[1]
        del particle_collection[0]
        for particle in particle_collection:
            particle.SetMaterial(\'My Particle Material\')

    Items in this list are of type :class:`RAParticle`.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self) -> str: ...
    def GetParticleNames(self) -> list[str]:
        """
        Get a list of the names of all the particles in this collection.

        :rtype: list
        """

    def GetParticle(self, particle_name: str) -> RAParticle:
        """
        Get a particle given its name.
        """

    def New(self) -> RAParticle: ...
