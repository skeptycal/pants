# Copyright 2018 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from dataclasses import dataclass

from pants.engine.rules import union
from pants.util.objects import enum


class Status(enum(['SUCCESS', 'FAILURE'])): pass


@dataclass(frozen=True)
class TestResult:
  status: Status
  stdout: str
  stderr: str

  # Prevent this class from being detected by pytest as a test class.
  __test__ = False


@union
class TestTarget:
  """A union for registration of a testable target type."""

  # Prevent this class from being detected by pytest as a test class.
  __test__ = False
