from framework.interface import InteractiveInterpreter

__version__ = '0.1'

def main():
  interpreter = InteractiveInterpreter()
  interpreter.cmdloop()

if __name__ == '__main__':
  main()
