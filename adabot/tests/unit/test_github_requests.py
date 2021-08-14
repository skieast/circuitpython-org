# The MIT License (MIT)
#
# Copyright (c) 2021 Michael Schroeder
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

"""Unit tests for 'adabot/github_requests.py'"""

# pylint: disable=protected-access

import pytest  # pylint: disable=unused-import

from adabot import github_requests


def test_fix_url():
    """Test URL fixing function."""
    url = github_requests._fix_url("/meta")
    assert url == "https://api.github.com/meta"


def test_fix_kwargs():
    """Test kwarg fixing function."""
    dummy_kwargs = github_requests._fix_kwargs({})

    assert "headers" in dummy_kwargs
    assert "Accept" in dummy_kwargs["headers"]
