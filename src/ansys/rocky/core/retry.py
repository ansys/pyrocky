# Copyright (C) 2023 - 2026 ANSYS, Inc. and/or its affiliates.
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

import time
from typing import Any, Callable


def wait_succeed(predicate_callback: Callable, *, timeout: int, expected_exc) -> Any:
    """
    Repeatedly calls ``predicate_callback`` until it succeeds or timeout is reached.

    Parameters
    ----------
    predicate_callback :
        Callable invoked until it returns successfully.
    timeout :
        Maximum wait time in seconds.
    expected_exc :
        Exception type to catch and retry while waiting.

    Returns
    -------
    Any
        The return value from ``predicate_callback``.

    Raises
    ------
    expected_exc
        Raised when retries exceed ``timeout``.
    """
    started = time.time()
    while True:
        try:
            return predicate_callback()
        except expected_exc as exc:
            if (time.time() - started) < timeout:
                time.sleep(1)
            else:
                raise exc
