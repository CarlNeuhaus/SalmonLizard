import cmd
import os
import sys
# user libraries
from framework.formatting import Bcolours
from databases.databaseSetup import Database

class InteractiveInterpreter(cmd.Cmd):
  def __init__(self):
      cmd.Cmd.__init__(self)
      self.prompt = Bcolours.OKBLUE + "lizard> " + Bcolours.ENDC
      self.intro = os.system("figlet lizard")
      self.myDatabase = Database()

  def do_use(self,line):
    options = line.split(None, 1)
    if options[0] == 'payload':
      payload = options[1]
    self.prompt = formatting.Bcolours.OKBLUE + options[0] + "-" + payload +  ">  " + formatting.Bcolours.ENDC
    pass

  def do_send(self,line):
    pass

  def complete_send(self,text,line,start_index,end_index):
    if text:
      return [
        address for address in self.myDatabase.addresses
        if address.startswith(text)
      ]
    else:
      return self.myDatabase.addresses

  def do_name(self,line):
     
    print "lists all names"
    pass

  def complete_name(self,text,line,start_index,end_index):
    if text:
      return [
        name for name in self.myDatabase.names
        if name.startswith(text)
      ]
    else:
      return self.myDatabase.names

  def do_clear(self,line):
    os.system('clear')
    pass

  def do_exit(self,line):
    os.system('clear')
    sys.exit()

if __name__ == '__main__':
  my_cmd = Complete()
  my_cmd.cmdloop()
