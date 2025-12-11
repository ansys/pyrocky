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

from _typeshed import Incomplete
from coilib50.element_function.semantic_association import (
    SemanticAssociation as SemanticAssociation,
)
from coilib50.units import IQuantity as IQuantity
from coilib50.units import Quantity as Quantity

from ansys.rocky.core._api_stubs.rocky30.plugins.api.ra_api import (
    RockyApiError as RockyApiError,
)

VALID_TYPES: Incomplete
VALID_SCOPE: Incomplete

class RACustomCurveAndGridProperty:
    """
    Helper class, to add, edit and remove custom curves and grid properties.

    .. code-block:: python

        particles = study.GetParticles()
        particles.AddCustomCurve(name='Custom Curve', scope='user', sources={'A': 'Particles Mass', 'B': 'Particles In Count'})
        particles.EditCustomCurve(edit_curve='Custom Curve', expression='A+B')
        particles.RemoveCustomCurve(name='Custom Curve')

        particles.AddCustomProperty(name='Property A', sources={'A': 'Coordinate : X', 'B': 'Coordinate : Y'})
        particles.EditCustomProperty(edit_property='Property A', new_name='New Property', expression='A*B')
        particles.RemoveCustomProperty(name='New Property')
    """

    def AddCustomCurve(
        self,
        name: str,
        curve_type: str = ...,
        output_unit: str = ...,
        scope: str = ...,
        sources: dict[str, str] | None = None,
        expression: str = "",
    ) -> None:
        """
        Add a custom curve in the database.
        :param name:
            The name of the curve to be set.
        :param curve_type:
            The type of the custom curve to be added.
        :param output_unit:
            The output unit, in which case the unit database will be queried for a quantity that makes sense.
            If None, the quantity is considered unknown.
        :param scope:
            The scope to be set.
        :param sources:
            A dict pointing the variable used to the curve association it represents and a
            string indicating in which unit the input data should be gotten.
        :param expression:
            The expression to be set.
        """

    def EditCustomCurve(
        self,
        edit_curve: str,
        new_name: str | None = None,
        sources: dict[str, str] | None = None,
        expression: str | None = None,
    ) -> None:
        """
        Edit a custom curve saved in the database.
        :param edit_curve:
            The name of the curve to be edited.
        :param new_name:
            The new name of the curve to be set.
        :param sources:
            A dict pointing the variable used to the curve association it represents and a
            string indicating in which unit the input data should be gotten.
        :param expression:
            The expression to be set.
        """

    def RemoveCustomCurve(self, name: str) -> None:
        """
        Remove the curve from the database
        :param name:
            The name of the curve to be removed.
        """

    def AddCustomProperty(
        self,
        name: str,
        property_type: str = ...,
        output_unit: str = ...,
        scope: str = ...,
        sources: dict[str, str] | None = None,
        expression: str = "",
    ) -> None:
        """
        Add a custom property to the database

        :param name:
            The name of the property to be set.
        :param property_type:
            The type of the custom property to be added.
        :param output_unit:
            The output unit, in which case the unit database will be queried for a quantity that makes sense.
            If None, the quantity is considered unknown.
        :param scope:
            The scope to be set.
        :param sources:
            A dict pointing the variable used to the property association it represents and a
            string indicating in which unit the input data should be gotten.
        :param expression:
            The expression to be set.
        """

    def EditCustomProperty(
        self,
        edit_property: str,
        new_name: str | None = None,
        sources: dict[str, str] | None = None,
        expression: str | None = None,
    ) -> None:
        """
        Edit a custom property saved in the database.
        :param edit_property:
            The name of the property to be edited.
        :param new_name:
            The new name of the property to be set.
        :param sources:
            A dict pointing the variable used to the property association it represents and a
            string indicating in which unit the input data should be gotten.
        :param expression:
            The expression to be set.
        """

    def RemoveCustomProperty(self, name: str) -> None:
        """
        Remove the property from the database
        :param name:
            The name of the property to be removed.
        """

class RACustomCurveParameters:
    variable_to_association_and_unit: dict[str, tuple[SemanticAssociation, str]]
    output_quantity: Incomplete
    domain_association: Incomplete
    def __init__(
        self, process: RACustomCurveAndGridProperty, sources: dict[str, str] | None = None
    ) -> None: ...
