#  salmon.py
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

__author__ = "Carl A Neuhaus"
__copyright__ = "Copyright 2015, Carl A Neuhaus"
__credits__ = ["zeroSteiner"]

__licence__ = "GNU Public Licence"
__version__ = "0.1b"
__maintainer__ = "Carl A Neuhaus"
__status__ = "test"

from framework.interface import InteractiveInterpreter

def main():
  interpreter = InteractiveInterpreter()
  interpreter.cmdloop()

if __name__ == '__main__':
  main()
