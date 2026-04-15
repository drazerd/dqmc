python_sources = [
  '__init__.py',
  '__main__.py',
  '_version.py',
  'data.py',
  'dqmc.py',
  'linalg.py',
  'logging.py',
  'measurements.py',
  'mfuncs.py',
  'model.py',
  'mp.py',
  'simulator.py',
]

py.install_sources(python_sources, subdir: 'dqmc')
py.install_sources(['src/__init__.py'], subdir: 'dqmc/src')

py.install_sources([
  'tests/__init__.py',
  'tests/test_dqmc.py',
  'tests/test_linalg.py',
  'tests/test_model.py',
  'tests/test_mp.py',
  'tests/test_sim.py',
  'tests/test_src.py'
], subdir: 'dqmc/tests')
