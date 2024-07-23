# Copyright (C) 2023 - 2024 ANSYS, Inc. and/or its affiliates.
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

from typing import List, Union

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)
from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_list import RAList as RAList

class RACFDPerParticleParameters(ApiElementItem):
    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetConvectiveHeatTransferLaw(self) -> str: ...
    def SetConvectiveHeatTransferLaw(self, value: str) -> None: ...
    def GetValidConvectiveHeatTransferLawValues(self) -> List[str]: ...
    def GetDragLaw(self) -> str: ...
    def SetDragLaw(self, value: str) -> None: ...
    def GetValidDragLawValues(self) -> List[str]: ...
    def GetLiftLaw(self) -> str: ...
    def SetLiftLaw(self, value: str) -> None: ...
    def GetValidLiftLawValues(self) -> List[str]: ...
    def GetMorsiAndAlexanderK1(self) -> float: ...
    def SetMorsiAndAlexanderK1(self, value: Union[str, float]) -> None: ...
    def GetMorsiAndAlexanderK2(self) -> float: ...
    def SetMorsiAndAlexanderK2(self, value: Union[str, float]) -> None: ...
    def GetMorsiAndAlexanderK3(self) -> float: ...
    def SetMorsiAndAlexanderK3(self, value: Union[str, float]) -> None: ...
    def GetSyamlalObrienC1(self) -> float: ...
    def SetSyamlalObrienC1(self, value: Union[str, float]) -> None: ...
    def GetSyamlalObrienD1(self) -> float: ...
    def SetSyamlalObrienD1(self, value: Union[str, float]) -> None: ...
    def GetTorqueLaw(self) -> str: ...
    def SetTorqueLaw(self, value: str) -> None: ...
    def GetValidTorqueLawValues(self) -> List[str]: ...
    def GetUseUserDefinedConstants(self) -> bool: ...
    def SetUseUserDefinedConstants(self, value: bool) -> None: ...
    def GetVirtualMassLaw(self) -> str: ...
    def SetVirtualMassLaw(self, value: str) -> None: ...
    def GetValidVirtualMassLawValues(self) -> List[str]: ...

class RACFDParametersList(RAList[RACFDPerParticleParameters]):
    @classmethod
    def GetWrappedClass(cls): ...
    @classmethod
    def GetClassName(cls): ...
    def GetParametersFor(self, particle): ...
    def New(self) -> None: ...
    def Remove(self, item) -> None: ...
    def Clear(self) -> None: ...
    def __delitem__(self, index) -> None: ...