"""Helper methods to wrap calls to the xdotool binary.

Eventually, this should wrap all available commands:
"""
import subprocess

class CommandWrapperMeta(type):
  """Defines meta attributes for the CommandWrapper class."""

  def __getattr__(cls, name):
    return lambda *args, **kwargs: cls.call(flags=kwargs, args=[name, *args])

class CommandWrapper(object, metaclass=CommandWrapperMeta):
  """Wraps a command (using subprocess.call)"""

  @classmethod
  def create(cls, name):
    """Creates an instance of CommandWrapper wrapping the command name."""
    return type(name, (CommandWrapper,), dict(_name=name))

  @property
  @classmethod
  def _name(cls):
    """Should be overriden by subclasses.

    The name of the command the class represents.
    """
    raise NotImplementedError()

  @classmethod
  def call(cls, flags=None, args=None):
    """Call the command using the array of specified flags and other args.

    flags -- A dictionary of flag name/argument pairs.  None for no argument.
    args -- Additional arguments to pass to the command.
    """
    if not args:
      args = []
    else:
      args = map(str, args)
    if not flags:
      flag_list = []
    else:
      flag_list = [
          str(arg) for argpair in [
              [flag, arg] if arg is not None else [flag]
              for flag, arg in flags.items()
          ] for arg in argpair
      ]
    subprocess.call([cls._name, *flag_list, *args])

