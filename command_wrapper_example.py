"""An example implementation of CommandWrapper for xdotool and ls"""
from command_wrapper import CommandWrapper
xdotool = CommandWrapper.create('xdotool')
ls = CommandWrapper.create('ls')

if __name__ == '__main__':
  xdotool.sleep(2)
  xdotool.type('slept for 2')
  ls.call(flags={'-la': None, '--block-size': 'M'})

