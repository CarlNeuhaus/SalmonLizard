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

try:
  from framework.template import LizardModule
  import ftplib
  import time
  from framework.formatting import coloursLinux as colours
  import thread
except Exception, error:
  print error

class Module(LizardModule):

    def run(self):
      hostnames = ["192.168.253.128","192.168.253.127","192.168.253.127","192.168.253.127","192.168.253.127","192.168.253.127","192.168.253.127","192.168.253.127","192.168.253.127","192.168.253.127"]
      name = "192.168.0.100"
      self.anonLogin(name)
      for hostname in hostnames:
        try:
          thread.start_new_thread(self.anonLogin, (hostname,))
        except Exception, e:
          print e
      return

    def anonLogin(self, hostname):
      try:
        ftp = ftplib.FTP(hostname)
        ftp.login('anonymous', 'me@you.com')
        print colours.OKGREEN + '\n[*] ' + str(hostname) + ' FTP Anonymous Logon Succeeded\n' + colours.ENDC
        ftp.quit()
      except:
        print colours.WARNING + '\n[-] ' + str(hostname) + ' FTP Anonymous Logon Failed\n' + colours.ENDC
  

     
    
