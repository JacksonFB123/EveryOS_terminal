class TerminalEmulator():
  def mode_win(self):
    print('"win" Selected')
    import os
    while 1:
      x = input('C:/>')
      if x == 'exitEmulation':
        break
      os.system(x)
  def mode_mac(self):
    print('"mac" Selected')
    import os
    while 1:
      x = input('Emulated-Macbook:~ guestaccount$ ')
      if x == 'exitEmulation':
        break
      os.system(x)
  def mode_linx(self):
    print('"linx" Selected')
    import os
    while 1:
      x = input('emulatedcomputer@linux:~$ ')
      if x == 'exitEmulation':
        break
      os.system(x)
TerminalEmulator = TerminalEmulator()
class Main():
  def execute(self, ays=False):
    if ays == True:
      while 1:
        print('EveryOS v1.0')
        print('What OS do you run?')
        print('Available Answers: win, mac, linx')
        x = input('    answer>>')
        if x == 'win':
          TerminalEmulator.mode_win()
        elif x == 'mac':
          TerminalEmulator.mode_mac()
        elif x == 'linx':
          TerminalEmulator.mode_linx()
        else:
          print('Wrong Choice! Please try again')
Main = Main()