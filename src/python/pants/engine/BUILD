# Copyright 2015 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

page(
  name='readme',
  source='README.md',
)

# TODO: Get rid of all these microtargets. The entire package should be one target,
# or be split into multiple packages.

python_library(
  name = 'legacy_engine',
  sources = ['legacy_engine.py', 'round_engine.py', 'round_manager.py'],
  dependencies = [
    '3rdparty/python/twitter/commons:twitter.common.collections',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:workunit',
    'src/python/pants/goal',
  ],
)

python_library(
  name='addressable',
  sources=['addressable.py'],
  dependencies=[
    ':objects',
    'src/python/pants/build_graph',
    'src/python/pants/util:memo',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='struct',
  sources=['struct.py'],
  dependencies=[
    ':addressable',
    ':objects',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='fs',
  sources=['fs.py'],
  dependencies=[
    '3rdparty/python/twitter/commons:twitter.common.collections',
    '3rdparty/python:dataclasses',
    ':objects',
    ':rules',
    ':selectors',
    'src/python/pants/base:project_tree',
    'src/python/pants/option',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='goal',
  sources=['goal.py'],
  dependencies=[
    '3rdparty/python:dataclasses',
    'src/python/pants/cache',
    'src/python/pants/option',
    'src/python/pants/util:memo',
    'src/python/pants/util:meta',
  ]
)

python_library(
  name='build_files',
  sources=['build_files.py'],
  dependencies=[
    ':addressable',
    ':fs',
    ':mapper',
    ':objects',
    ':selectors',
    ':struct',
    'src/python/pants/base:project_tree',
    'src/python/pants/build_graph',
    'src/python/pants/util:collections',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:filtering',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='mapper',
  sources=['mapper.py'],
  dependencies=[
    '3rdparty/python:dataclasses',
    ':objects',
    ':parser',
    'src/python/pants/build_graph',
    'src/python/pants/util:objects',
    'src/python/pants/util:memo',
  ]
)

python_library(
  name='isolated_process',
  sources=['isolated_process.py'],
  dependencies=[
    ':fs',
    ':rules',
    ':selectors',
    ':platform',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='nodes',
  sources=['nodes.py'],
  dependencies=[
    '3rdparty/python/twitter/commons:twitter.common.collections',
    '3rdparty/python:dataclasses',
    ':addressable',
    ':fs',
    ':struct',
    'src/python/pants/base:project_tree',
    'src/python/pants/build_graph',
  ]
)

python_library(
  name='objects',
  sources=['objects.py'],
  dependencies=[
    'src/python/pants/util:memo',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='parser',
  sources=['parser.py'],
  dependencies=[
    '3rdparty/python:dataclasses',
    ':addressable',
    ':objects',
    'src/python/pants/build_graph',
    'src/python/pants/util:memo',
  ]
)

python_library(
  name='platform',
  sources=['platform.py'],
  dependencies=[
      ':rules',
      'src/python/pants/util:objects',
      'src/python/pants/util:memo',
      'src/python/pants/util:osutil',
  ]
)

python_library(
  name='rules',
  sources=['rules.py'],
  dependencies=[
    '3rdparty/python:asttokens',
    '3rdparty/python/twitter/commons:twitter.common.collections',
    ':goal',
    ':selectors',
    'src/python/pants/base:specs',
    'src/python/pants/util:collections',
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='selectors',
  sources=['selectors.py'],
  dependencies=[
    'src/python/pants/util:objects',
  ]
)

python_library(
  name='scheduler',
  sources=['scheduler.py'],
  dependencies=[
    '3rdparty/python/twitter/commons:twitter.common.collections',
    '3rdparty/python:dataclasses',
    ':fs',
    ':isolated_process',
    ':native',
    ':nodes',
    ':objects',
    ':rules',
    'src/python/pants/base:exceptions',
    'src/python/pants/base:specs',
    'src/python/pants/build_graph',
    'src/python/pants/rules/core:core',
  ]
)

python_library(
  name='native',
  sources=['native.py'],
  dependencies=[
    ':native_engine_shared_library',
    ':selectors',
    '3rdparty/python:cffi',
    '3rdparty/python:setuptools',
    'src/python/pants/binaries',
    'src/python/pants/util:dirutil',
    'src/python/pants/util:memo',
    'src/python/pants/util:objects'
  ],
)


python_library(
  name='console',
  sources=['console.py'],
  dependencies=[
    '3rdparty/python:ansicolors',
  ],
)

resources(
  name='native_engine_shared_library',
  sources=['native_engine.so']
)
