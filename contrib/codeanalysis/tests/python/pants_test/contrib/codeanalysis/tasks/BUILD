# Copyright 2017 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).


python_tests(
  name = 'integration',
  sources = globs('*_integration.py'),
  dependencies=[
    'tests/python/pants_test:int-test',
    'examples/src/java/org/pantsbuild/example:hello_directory',
  ],
  tags={'integration'},
  timeout=240,
)
