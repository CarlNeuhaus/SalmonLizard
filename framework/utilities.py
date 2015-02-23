#framework/utilities.py

import os
import itertools

class Namespace:
    """
    This class is used to hold attributes of the framework. It doesn't
    really do anything, it's used for organizational purposes only.
    """
    pass

class Filewalker:
  def __init__(self, filespath, absolute_path=False, skip_files=False, skip_dirs=False, filter_func=None):

    if not (os.path.isfile(filespath) or os.path.isdir(filespath)):
      print(filespath + ' is neither a file or directory')
    if absolute_path:
      self.filespath = os.path.abspath(filespath)
    else:
      self.filespath = os.path.relpath(filespath)
    self.skip_files = skip_files
    self.skip_dirs = skip_dirs
    self.filter_func = filter_func
    if os.path.isdir(self.filespath):
      self.__iter__ = self.next_dir
    elif os.path.isfile(self.filespath):
      self.__iter__ = self.next_file

  def skip(self, curFile):
    if self.skip_files and os.path.isfile(curFile):
      return True
    if self.skip_dirs and os.path.isdir(curFile):
      return True
    if self.filter_func != None:
      if not self.filter_func(curFile):
        return True
    return False

  def next_dir(self):
    for root, dirs, files in os.walk(self.filespath):
      for curFile in files:
        curFile = os.path.join(root, curFile)
        if not self.skip(curFile):
          yield curFile
      for curDir in dirs:
          curDir = os.path.join(root,curDir)
          if not self.skip(curDir):
            yield curDir
    raise StopIteration

  def next_file(self):
    if not self.skip(self.filespath):
      yield self.filespath
    raise StopIteration

