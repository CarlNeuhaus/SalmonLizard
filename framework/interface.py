#  formatting/interface.py
#
#  Copyright 2015 Carl A. Neuhaus
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

import cmd
import os
import sys
# user libraries
# fixes colours 
if sys.platform == 'darwin':
  from framework.formatting import coloursOSX as colours
if sys.platform == 'linux':
  from framework.formatting import coloursLinux as colours
if sys.platform == 'win32':
  from framework.formatting import coloursWindows as colours

from framework.databaseSetup import Database
class InteractiveInterpreter(cmd.Cmd):
  def __init__(self):
      cmd.Cmd.__init__(self)
      self.prompt = colours.OKBLUE + "lizard> " + colours.ENDC
      self.intro = os.system("figlet lizard")
      self.myDatabase = Database()

  def do_use(self,line):
    options = line.split(None, 1)
    if options[0] == 'payload':
      payload = options[1]
    self.prompt = colours.OKBLUE + options[0] + "-" + payload +  ">  " + colours.ENDC
    pass

  def do_send(self,line):
    pass

  def complete_send(self,text,line,start_index,end_index):
    if text:
      return [
        address for address in self.myDatabase.addresses()
        if address.startswith(text)
      ]
    else:
      return self.myDatabase.addresses()

  def do_name(self,line):
    print "lists all names"
    pass

  def complete_name(self,text,line,start_index,end_index):
    if text:
      return [
        name for name in self.myDatabase.names()
        if name.startswith(text)
      ]
    else:
      return self.myDatabase.names()

  def do_clear(self,line):
    os.system('clear')
    pass

  def do_exit(self,line):
    os.system('clear')
    sys.exit()

if __name__ == '__main__':
  my_cmd = Complete()
  my_cmd.cmdloop()
