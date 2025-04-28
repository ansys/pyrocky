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

# (C) 2024 ANSYS, Inc. Unauthorized use, distribution, or duplication is prohibited.
from collections.abc import Generator
from typing import Generic, TypeVar

from ansys.rocky.core._api_stubs.plugins10.plugins.api.api_element_item import (
    ApiElementItem,
)

T = TypeVar("T", bound=ApiElementItem)

class RAList(ApiElementItem, Generic[T]):
    """
    Base class for API classes that wrap SubjectLists (and related list classes).

    Provides methods to add, remove and iterate on the items. The PrePost Scripting wrappers for the list items
    will be obtained via ApiApplication._GetElementWrapper(), so it's important that these wrappers
    are registered as wrapper classes (see `EPApiExtension`).
    """

    def New(self) -> T:
        """
        Add a new item. Returns the newly created item.
        """
        from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import CheckResults

        CheckResults(self)

        element = self.subject.New()
        return self._GetApplication()._GetElementWrapper(
            element.id, element, self._model_id
        )

    def Remove(self, item: T) -> None:
        """
        Remove an item from the list.
        """
        from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import CheckResults

        CheckResults(self)

        if isinstance(item, ApiElementItem):
            item = item.subject

        self.subject.Remove(item)

    def Clear(self) -> None:
        """
        Remove all items from the list.
        """
        from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import CheckResults

        CheckResults(self)

        self.subject.Clear()

    def __len__(self) -> int:
        return len(self.subject)

    def __getitem__(self, index: int) -> T:
        from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import RockyApiError

        if index >= len(self):
            raise RockyApiError(f"Invalid index: {index}")

        item = self.subject[index]
        return self._GetApplication()._GetElementWrapper(item.id, item, self._model_id)

    def __iter__(self) -> Generator[T, None, None]:
        for item in self.subject:
            yield self._GetApplication()._GetElementWrapper(item.id, item, self._model_id)

    def __delitem__(self, index: int) -> None:
        from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import CheckResults

        CheckResults(self)

        del self.subject[index]
