"""
Class:  Asshdb, Alias

"""
import yaml
import re
import sys
from shutil import copyfile
from types import *

# create alias object
# asshdb should have list of alias objects
#    add/edit/delete alias objects

## alias object
# get object
# make sure alias, aliasname, and serverAddress are defined

class Asshdb(object):
    'Responsible for managing and resolving alias records'
    Name = "Asshdb"
    aliases = {}
    asshdb = {}
    AsshConfig = None

    def __init__(self, configObj):
        ## Convert aliases into objects
        self.asshConfig = configObj
        self.loadAsshdb(self.asshConfig.config['asshdb'])
        
        for k in self.asshdb:
            Asshdb.aliases[k] = Alias(self.asshdb[k])

    def loadAsshdb(self, asshdbfile):
        try:
            with open(asshdbfile) as f:
                self.asshdb = yaml.load(f)
        except IOError as e:
            print('Alias Database file not found:' + asshdbfile)
            ##print 'Using empty alias list.'
            sys.exit()

    def saveAsshdb(self, asshdbfile):
        
        ## Convert aliases to dict
        self.asshdb = {}
        for k in self.aliases:
            self.asshdb[k] = self.aliases[k].__dict__

        ## make a copy of the asshdb file before overwriting it
        copyfile(self.asshConfig.config['asshdb'], self.asshConfig.configDir + '/asshdb.yml.bak')

        try:
            with open(asshdbfile, 'w') as f:
                yaml.dump(self.asshdb, f, default_flow_style=False)
        except IOError as e:
            print('Could not save Alias DB file:' + asshdbfile)
            sys.exit()

    def save(self):
        self.saveAsshdb(self.asshConfig.config['asshdb'])
    
    def delete(self, alias):
        if self.checkAlias(alias):
            del self.aliases[alias]

    def add(self, alias_dict):
        self.aliases[alias_dict['aliasName']] = Alias(alias_dict)

    def printAlias(self, alias):
        if self.checkAlias(alias):
            print("Alias: " + alias)
            for k,v in vars(self.aliases[alias]).items():
                print(" " , k , ": " , v)
            print("")
        else:
            print("Alias not found: " + alias)
    
    def checkAlias(self, alias):
        if alias in self.aliases:
            return True
        else:
            return False

    def aliasMatches(self, alias):
        for k in self.aliases:
            matchObj = re.match(alias, k, flags=0)
            if matchObj:
                self.printAlias(k)

class Alias(object):
    'manage alias objects'
    Name = "Alias"

    def __init__(self, opt_dict = {}):
        self.aliasDesc = ''           # Alias description field
        self.aliasType = 'ssh'        # ssh only supported
        self.bulkSshArgs = None       # *for now use bulk options
        self.sshUser =   None         # user to connect as
        self.sshHostname = None
        
        for k in opt_dict:
            self.setOption(k, opt_dict[k])
        
    def setOption(self, option, value):
        if hasattr(self, option):
            setattr(self, option, value)
        else:
            print("Alias Attribute not found: " + option)

    def aliasDict(self):
        print(self.__dict__)
        
        
