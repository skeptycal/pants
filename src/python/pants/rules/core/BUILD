python_library(
    dependencies = [
      '3rdparty/python:dataclasses',
      'src/python/pants/base:exiter',
      'src/python/pants/build_graph',
      'src/python/pants/engine:goal',
      'src/python/pants/engine:rules',
      'src/python/pants/engine:selectors',
      'src/python/pants/engine:addressable',
      'src/python/pants/engine:console',
      'src/python/pants/engine/legacy:graph',
      'src/python/pants/goal',
      'src/python/pants/source',
    ]
)

python_tests(
  name = "tests",
  dependencies = [
    ':core',
    'tests/python/pants_test:console_rule_test_base',
    'tests/python/pants_test/engine:util'
  ]
)

