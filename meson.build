project('dqmc', ['c'],
  version : '0.1.0',
  default_options : [
    'warning_level=1',
  ]
)

py = import('python').find_installation(pure: false)
py_dep = py.dependency()

incdir_numpy = run_command(
  py,
  ['-c', 'import numpy; print(numpy.get_include())'],
  check : true
).stdout().strip()

inc_np = include_directories(incdir_numpy)

subdir('dqmc')
