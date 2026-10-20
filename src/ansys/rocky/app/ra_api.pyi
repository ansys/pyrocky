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

from rocky30.models.study.study import Study as Study

from ansys.rocky.app.api_element_item import ApiError

class RockyApiError(ApiError):
    """
    Exception class representing an error generated in the API layer.

    RockyApiErrors should be raised for circumstances that are known to be user errors and not
    software bugs - things like trying to make a setup change without deleting results beforehand,
    trying to remove by name items that don't exist, etc.
    """

def CheckCanModify(ra_object) -> None:
    """
    Helper function that checks if a property can be changed by evaluating two conditions:

    1) If the project has simulation results, raises an error with a helpful message. Should be called by API methods
    that would invalidate simulation results;
    2) If we are in a blocked context, i.e. the `ValidateModuleInput`, no property should be changed.
    """

def CheckPropAffectsSimulation(prop_owner, prop_name) -> bool:
    """
    Helper function to check if the property (given by prop_name) affects the simulation results.
    """

def IsObjectUsedByRestart(subject) -> bool: ...
def IsFreeflow(raise_error: bool = True) -> bool:
    """
    Helper method to be used to ensure the app is in freeflow variant.
    """
