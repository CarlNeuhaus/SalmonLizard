# framework.core.py

import os

from framework.utilities import Namespace, Filewalker

class Framework(object):

  def __init__(self):
    self.modules = {}
    self.__package__ = '.'.join(self.__module__.split('.')[:-1])
    package_path = __import__(self.__package__, None, None, ['__path__']).__path__[0]
    self.directories = Namespace()
    self.directories.modules_path = package_path + os.sep + 'modules' + os.sep
    
    # setup to load modules
    modules_path = self.directories.modules_path
    print "Searching for modules in: " + modules_path
    self.current_module = None
    if not os.path.isdir(modules_path):
      print 'path to modules not found'
    for module_path in Filewalker(modules_path, absolute_path=True, skip_dirs=True):
      module_path = module_path.replace(os.path.sep, '/')
      if not module_path.endswith('.py'):
        continue
      print module_path
      module_path = module_path[len(modules_path):-3]
      module_name = module_path.split(os.path.sep)[-1]
      if module_name.startswith('__'):
        continue
      if module_name.lower() != module_name:
        continue
    # load modules
      try:
        module_instance = self.import_module(module_path)
      except:
        print "failed"
      if not hasattr(module_instance, 'run'):
        print ('module: ' + module_path + ' has no run() method')
      module_instance.name = module_name
      module_instance.path = module_path
      self.modules[module_path] = module_instance
      #print "Loaded " + str(len(self.modules)) + " modules into framework"
    return

  def import_module(self, module_path, reload_module=False):
    try:
      module = __import__(self.__package__ + '.modules.' + module_path.replace('/', '.'), None, None, ['Module'])
      #module_instance = module.Module(self)
      module_instance = module
    except Exception as err:
      message = 'failed to load module: ' + module_path
      print message 
    return module_instance
  
  def run(self, module=None):
    if module == None:
      module = self.current_module
      print module
    result = None
    try:
      result = module.run()
    except KeyboardInterrupt as error:
      raise error
    return result
