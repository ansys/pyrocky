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

from rocky30.models.contact_data.contact_data_process import (
    ContactDataProcessSubject as ContactDataProcessSubject,
)
from rocky30.models.particle_joints_data.particle_joints_data_process import (
    ParticleJointsProcessSubject as ParticleJointsProcessSubject,
)
from rocky30.models.sph.sph_eulerian_solution import (
    SPHEulerianSolution as SPHEulerianSolution,
)

from ansys.rocky.app.api_element_item import ApiElementItem
from ansys.rocky.app.ra_api import RockyApiError as RockyApiError

class RAOutputData(ApiElementItem):
    """
    Rocky PrePost Scripting wrapper to manipulate the Output Data.

    .. code-block:: python

        output_data = study.GetOutputData()
        # To enabled/disabled individual properties:
        output_data.SetStandardOutputPropertyEnabled('Geometries', 'Area : Cell', enabled=False)
        # To enabled/disabled all properties under a root parent:
        output_data.SetStandardOutputPropertyEnabled('Geometries', enabled=False)

    """

    @classmethod
    def GetWrappedClass(cls) -> type: ...
    @classmethod
    def GetClassName(cls) -> str: ...
    def GetStandardOutputPropertyEnabled(self, *output_property: str) -> bool:
        """
        Retrieve enable state of given "Standard Output Property".

        :param output_property:
            The output property name.
        """

    def SetStandardOutputPropertyEnabled(
        self, *output_property: str, enabled: bool
    ) -> None:
        """
        Set enable state of given "Standard Output Property".

        :param output_property:
            The output property name.
        :param enabled:
            The enable state of given "Standard Output Property".
        """

    def GetAdditionalOutputPropertyEnabled(self, *output_property: str) -> bool:
        """
        Retrieve enable state of given "Additional Output Property".

        :param output_property:
            The output property name.
        """

    def SetAdditionalOutputPropertyEnabled(
        self, *output_property: str, enabled: bool
    ) -> None:
        """
        Set enable state of given "Additional Output Property".

        :param output_property:
            The output property name.
        :param enabled:
            The enable state of given "Additional Output Property".
        """

    def GetModulesOutputPropertyEnabled(self, *output_property: str) -> bool:
        """
        Retrieve enable state of given "Modules Output Property".

        :param output_property:
            The output property name.
        """

    def SetModulesOutputPropertyEnabled(
        self, *output_property: str, enabled: bool
    ) -> None:
        """
        Set enable state of given "Modules Output Property".

        :param output_property:
            The output property name.
        :param enabled:
            The enable state of given "Modules Output Property".
        """

    @staticmethod
    def GetAvailableStandardOutputProperties() -> dict:
        """
        :returns: The available "Standard Output Properties".
        """

    @staticmethod
    def GetAvailableModulesOutputProperties() -> dict:
        """
        :returns: The available "Modules Output Properties".
        """

    def GetStandardOutputPropertiesData(self) -> dict:
        """
        :returns: The current value of "Standard Output Properties".
        """

    def SetStandardOutputPropertiesData(self, data_dict: dict) -> None:
        """
        Set the current value of "Standard Output Properties".

        :param data_dict:
            The data dictionary to set.
        """

    def GetModulesOutputPropertiesData(self) -> dict:
        """
        :returns: The current value of "Modules Output Properties".
        """

    def SetModulesOutputPropertiesData(self, data_dict: dict) -> None:
        """
        Set the current value of "Modules Output Properties".

        :param data_dict:
            The data dictionary to set.
        """

    def RestoreOutputPropertiesDefaults(self) -> None:
        """
        Restore default values of "Output Properties".
        """

    def GetCollectJointData(self) -> bool:
        """
        Get the value of "Collect Joint Data".

        """

    def SetCollectJointData(self, value: bool) -> None:
        """
        Set the value of "Collect Joint Data".

        :param value:
            The value to set.
        """

    def EnableCollectJointData(self) -> None:
        """
        Set the value of "Collect Joint Data" to True.
        """

    def DisableCollectJointData(self) -> None:
        """
        Set the value of "Collect Joint Data" to False.
        """

    def IsCollectJointDataEnabled(self) -> bool:
        """
        Check if the "Collect Joint Data" is enabled.

        """

    def GetCollectContactsData(self) -> bool:
        """
        Get the value of "Collect Contacts Data".

        """

    def SetCollectContactsData(self, value: bool) -> None:
        """
        Set the value of "Collect Contacts Data".

        :param value:
            The value to set.
        """

    def EnableCollectContactsData(self) -> None:
        """
        Set the value of "Collect Contacts Data" to True.
        """

    def DisableCollectContactsData(self) -> None:
        """
        Set the value of "Collect Contacts Data" to False.
        """

    def IsCollectContactsDataEnabled(self) -> bool:
        """
        Check if the "Collect Contacts Data" is enabled.

        """

    def GetIncludeAdhesiveContacts(self) -> bool:
        """
        Get the value of "Include Adhesive Contacts".

        """

    def SetIncludeAdhesiveContacts(self, value: bool) -> None:
        """
        Set the value of "Include Adhesive Contacts".

        :param value:
            The value to set.
        """

    def EnableIncludeAdhesiveContacts(self) -> None:
        """
        Set the value of "Include Adhesive Contacts" to True.
        """

    def DisableIncludeAdhesiveContacts(self) -> None:
        """
        Set the value of "Include Adhesive Contacts" to False.
        """

    def IsIncludeAdhesiveContactsEnabled(self) -> bool:
        """
        Check if the "Include Adhesive Contacts" is enabled.

        """

    def GetSphEulerianSolutionEnabled(self) -> bool:
        """
        Delegates the method to the project sph settings.
        """

    def SetSphEulerianSolutionEnabled(self, value: bool) -> None:
        """
        Delegate the method to the project sph settings.

        :param value:
            The value to set.
        """

    def EnableSphEulerianSolution(self) -> None:
        """
        Set the value of "Eulerian Solution" to True.
        """

    def DisableSphEulerianSolution(self) -> None:
        """
        Set the value of "Eulerian Solution" to False.
        """

    def IsSphEulerianSolutionEnabled(self) -> bool:
        """
        Check if the "Eulerian Solution" is enabled.

        """
