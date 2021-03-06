# Copyright © 2021 by Shun Huang. All rights reserved.
# Licensed under MIT License.
# See LICENSE in the project root for license information.

"""Tree Exception Definitions."""


class EmptyTreeError(Exception):
    """Raised when a tree is empty."""

    def __init__(self):
        Exception.__init__(self, "The tree is empty.")


class DuplicateKeyError(Exception):
    """Raised when a key already exists."""

    def __init__(self, key):
        Exception.__init__(self, f"{key} already exists.")


class KeyNotFoundError(Exception):
    """Raised when a key does not exist."""

    def __init__(self, key):
        Exception.__init__(self, f"{key} does not exist.")
