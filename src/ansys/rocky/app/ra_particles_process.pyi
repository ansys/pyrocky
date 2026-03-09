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

from ansys.rocky.app.ra_grid_process_element import (
    RAGridProcessElementItem as RAGridProcessElementItem,
)

class RAParticles(RAGridProcessElementItem):
    """
    Rocky api Particles model.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def GetNumberOfParticles(self, time_step):
        """
        Get the number of active particles at the given time step.

        :type time_step: unicode, ITimeStep or int
        :param time_step:
            Either a 'current' string with meaning the current time step
            or an ITimeStep identifying the time to get the topology shape
            or an int identifying the time step index to be used based on the global time set

        :rtype: int
        :returns:
            The number of particles
        """

    def IterParticles(self, time_step):
        """
        Iterate on the active particles at the given time step.

        :type time_step: unicode, ITimeStep or int
        :param time_step:
            Either a 'current' string with meaning the current time step
            or an ITimeStep identifying the time to get the topology shape
            or an int identifying the time step index to be used based on the global time set

        :rtype: iterator(Particle)
        :returns:
            An iterator over the particles.
            A Particle has:
            - x, y, z, size
            - x_axis, y_axis, z_axis, orientation_angle
        """

    def RemoveProcess(self) -> None:
        """
        It is not possible to remove the item "Particles" from the project. It\'s a standard Rocky
        item in project.
        """
