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

class RAContactData(RAGridProcessElementItem):
    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def RemoveProcess(self) -> None:
        """
        It is not possible to remove the item "Contacts" from the project. It\'s a standard Rocky
        item in project.
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
