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
from ansys.rocky.app.ra_point_cloud import RAPointCloud as RAPointCloud

class RAPointCloudCollection(RAList[RAPointCloud]):
    """
    Rocky PrePost Scripting wrapper for the collection of point clouds in a project.

    This wrapper corresponds to the "Point Clouds" item in the project\'s data tree. To retrieve the
    :class:`RAPointCloudCollection` from a :class:`RAStudy`, use:

    .. code-block:: python

        point_cloud_collection = study.GetPointCloudCollection()

    Instances of the :class:`RAPointCloudCollection` class act as regular Python lists, and can be
    iterated on, accessed via index, etc:

    .. code-block:: python

        point_cloud_1 = point_cloud_collection.New()
        point_cloud_2 = point_cloud_collection[1]
        del point_cloud_collection[0]

    Items in this list are of type :class:`RAPointCloud`.
    """

    @classmethod
    def GetWrappedClass(self): ...
    @classmethod
    def GetClassName(self): ...
