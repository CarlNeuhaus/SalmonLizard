# framework/modules/ftp_login.py

#class Bruteforce:
#  def __init__(self, dictonary_path=None):
#    if dictonary_path == None:
#      self.dictonary = None
#    else:
#      self.dictonary = open(dictonary_path, 'r')
#
#  def __iter__(self):
#    if self.dictonary == None:
#      for password in StringGenerator(20):
#        yield password
#    else:
#        password = self.dictonary.readline()
#        while password:
#          yeild password
#          password = self.dictonary.readline()
#        self.dictonary.close()
#    raise StopIteration

class Module:
    def run(self):
      print "hello"
