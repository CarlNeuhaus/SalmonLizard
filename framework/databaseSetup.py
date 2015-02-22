#  databases/databaseSetup.py
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

class Database():

  def names(self):
    with open('databases/names.db') as names_database:
      names = [line.rstrip('\n') for line in names_database]
      return names

  def addresses(self):
    with open('databases/addresses.db') as addresses_database:
      addresses = [line.rstrip('\n') for line in addresses_database]
      return addresses
