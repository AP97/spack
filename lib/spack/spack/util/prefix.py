"""
This file contains utilities to help with installing packages.
"""
from spack.util.filesystem import new_path

class Prefix(object):
    """This class represents an installation prefix, but provides useful
       attributes for referring to directories inside the prefix.

       For example, you can do something like this::

           prefix = Prefix('/usr')
           print prefix.lib
           print prefix.lib64
           print prefix.bin
           print prefix.share
           print prefix.man4

       This program would print:

           /usr/lib
           /usr/lib64
           /usr/bin
           /usr/share
           /usr/share/man/man4

       In addition, Prefix objects can be added to strings, e.g.:

           print "foobar " + prefix

       This prints 'foobar /usr". All of this is meant to make custom
       installs easy.
    """

    def __init__(self, prefix):
        self.prefix = prefix
        self.bin     = new_path(self.prefix, 'bin')
        self.sbin    = new_path(self.prefix, 'sbin')
        self.etc     = new_path(self.prefix, 'etc')
        self.include = new_path(self.prefix, 'include')
        self.lib     = new_path(self.prefix, 'lib')
        self.lib64   = new_path(self.prefix, 'lib64')
        self.libexec = new_path(self.prefix, 'libexec')
        self.share   = new_path(self.prefix, 'share')
        self.doc     = new_path(self.share, 'doc')
        self.info    = new_path(self.share, 'info')
        self.man     = new_path(self.share, 'man')
        self.man1    = new_path(self.man, 'man1')
        self.man2    = new_path(self.man, 'man2')
        self.man3    = new_path(self.man, 'man3')
        self.man4    = new_path(self.man, 'man4')
        self.man5    = new_path(self.man, 'man5')
        self.man6    = new_path(self.man, 'man6')
        self.man7    = new_path(self.man, 'man7')
        self.man8    = new_path(self.man, 'man8')


    def __str__(self):
        return self.prefix


    def __add__(self, other):
        return str(self) + other


    def __radd__(self, other):
        return other + str(self)
