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

from ansys.rocky.app.ra_list import RAList as RAList
from ansys.rocky.app.ra_materials_interaction import (
    RAMaterialsInteraction as RAMaterialsInteraction,
)

class RAMaterialsInteractionCollection(RAList[RAMaterialsInteraction]):
    """
    Rocky PrePost Scripting wrapper for the collection of materials interactions in a project.

    This wrapper corresponds to the "Materials Interactions" item on the project\'s data tree. Retrieve
    the :class:`RAMaterialsInteractionCollection` from a :class:`RAStudy` via:

    .. code-block:: python

        interaction_collection = RAMaterialCollection.GetMaterialsInteractionCollection()

    Instances of the :class:`RAMaterialsInteractionCollection` class act as regular Python lists and can be
    iterated on, individual materials accessed via index, etc:

    .. code-block:: python

        interaction_1 = interaction_collection[3]
        for interaction in interaction_collection:
            interaction.SetAdhesiveFraction(80, \'%\')
        interaction_2 = interaction_collection.GetMaterialsInteraction(\'Default Particles\', \'Default Boundaries\')

    Note that individual interactions can\'t be created or removed by the user: they are created and
    removed as necessary as new materials are created or removed.

    Items in this list are of type :class:`RAMaterialsInteraction`.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
    def New(self) -> None:
        """
        Unused: Materials Interactions are automatically created when Materials are created.
        """

    def __delitem__(self, index) -> None:
        """
        Unused: Materials Interactions are automatically deleted when Materials are created.
        """

    def Remove(self, item) -> None:
        """
        Unused: Materials Interactions are automatically deleted when Materials are created.
        """

    def Clear(self) -> None:
        """
        Unused: Materials Interactions are automatically deleted when Materials are created.
        """

    def GetMaterialsInteraction(self, material_1, material_2) -> RAMaterialsInteraction:
        """
        Get the materials interaction for the given pair of materials.

        For both `material_1` and `material_2` parameters, the parameter can be either an instance
        of :class:`RASolidMaterial` or the material's name.
        """
