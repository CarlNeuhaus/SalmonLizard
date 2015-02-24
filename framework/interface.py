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
if sys.platform == 'linux' or sys.platform == 'linux2':
  from framework.formatting import coloursLinux as colours
if sys.platform == 'win32':
  from framework.formatting import coloursWindows as colours

from framework.databaseSetup import Database
from framework.core import Framework

class InteractiveInterpreter(cmd.Cmd):
  def __init__(self):
      cmd.Cmd.__init__(self)
      self.prompt = colours.OKBLUE + "lizard> " + colours.ENDC
      self.intro = os.system("figlet lizard")
      self.myDatabase = Database()
      self.frmwk = Framework()
      print "Loaded Modules: " + ', '.join(self.frmwk.modules.keys())

  def do_use(self,line):
    """Select a module to use"""
    line = line.split(' ')
    module_name = line[0]
    if module_name in self.frmwk.modules.keys():
      self.frmwk.current_module = self.frmwk.modules[module_name]    
    else:
      print "Failed to load: " + module_name

  def complete_use(self, text, line, start_index, end_index):
    return [
      module for module in self.frmwk.modules.keys()
      if module.startswith(text)
    ]

  def do_run(self, line):
    """Run selected module"""
    line = line.split(' ')
    old_module = None
    if line[0] in self.frmwk.modules.keys():
      old_module = self.frmwk.current_module
      self.frmwk.current_module = self.frmwk.modules[line[0]]
    if self.frmwk.current_module == None:
      print "Must use module first"
      return
    module = self.frmwk.current_module
    try:
      self.frmwk.run()
    except KeyboardInterrupt:
      print ''
    except Exception as error:
      old_module = None
      print "shit broke"
    if old_module:
      self.frmwk.current_module = old_module

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
