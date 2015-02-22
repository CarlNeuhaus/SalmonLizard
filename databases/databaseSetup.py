class Database():

  def names(self):
    with open('databases/names.db') as names_database:
      names = [line.rstrip('\n') for line in names_database]
      return names

  def addresses(self):
    with open('databases/addresses.db') as addresses_database:
      addresses = [line.rstrip('\n') for line in addresses_database]
      return addresses
