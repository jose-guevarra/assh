"""
Class:  Aliasdb, Alias

"""
import yaml
import re
import sys
from shutil import copyfile
from types import *

# create alias object
# aliasdb should have list of alias objects
#    add/edit/delete alias objects

## alias object
# get object
# make sure alias, aliasname, and serverAddress are defined

class Aliasdb(object):
    'Responsible for managing and resolving alias records'
    Name = "Aliasdb"
    aliases = {}
    aliasdb = {}
    AsshConfig = None

    def __init__(self, configObj):
        ## Convert aliases into objects
        self.asshConfig = configObj
        self.loadAliasdb(self.asshConfig.config['aliasdb'])
        
        for k in self.aliasdb:
            Aliasdb.aliases[k] = Alias(self.aliasdb[k])

    def loadAliasdb(self, aliasdbfile):
        try:
            with open(aliasdbfile) as f:
                self.aliasdb = yaml.load(f)
        except IOError as e:
            print 'Alias Database file not found:' + aliasdbfile
            ##print 'Using empty alias list.'
            sys.exit()

    def saveAliasdb(self, aliasdbfile):
        
        ## Convert aliases to dict
        self.aliasdb = {}
        for k in self.aliases:
            self.aliasdb[k] = self.aliases[k].__dict__

        ## make a copy of the aliasdb file before overwriting it
        copyfile(self.asshConfig.config['aliasdb'], self.asshConfig.configDir + '/aliasdb.yaml.bak')

        try:
            with open(aliasdbfile, 'w') as f:
                yaml.dump(self.aliasdb, f, default_flow_style=False)
        except IOError as e:
            print 'Could not save Alias DB file:' + aliasdbfile
            sys.exit()

    def save(self):
        self.saveAliasdb(self.asshConfig.config['aliasdb'])
    
    def delete(self, alias):
        if self.checkAlias(alias):
            del self.aliases[alias]

    def add(self, alias_dict):
        ##@todo: make sure required fields are filled
        self.aliases[alias_dict['aliasName']] = Alias(alias_dict)

    def printAlias(self, alias):
        if self.checkAlias(alias):
            ##@todo: add sorting by key
            for k,v in self.aliases[alias].__dict__.iteritems():
                if v:
                    if type(v) is BooleanType:
                        boolstr = 'True' if v else 'False'
                        print " " + k + ": " + boolstr
                    else:
                        print " " + k + ": " + v
                else:
                    print " " + k + ": " 
            print ""
        else:
            print "Alias not found: " + alias
    
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
        self.aliasName = None         # name of the alias
        self.aliasdesc = ''           # Alias description field
        self.aliasType = 'ssh'          # ssh, cmd, container
        self.bulkSshArgs = None       ## for now use bulk options
        self.sshUser =   None             # user to connect as
        self.sshHostname = None
        self.sshCommand = None
        self.Command = None
        self.sshVersion = None        # ssh version -X 
        self.sshCompression = False    # ssh -C
        self.gtUseGt = None          # open in new gnome-terminal (otherwise just ssh)
        self.gtProfile = None         # a test gnome-terminal option
        self.gtNewWindow = None       # tab,window,none
        self.gtCommand = None
        
        for k in opt_dict:
            self.setOption(k, opt_dict[k])
        
    def setOption(self, option, value):
        if hasattr(self, option):
            setattr(self, option, value)
        else:
            print "Alias Attribute not found: " + option

    def aliasDict(self):
        print self.__dict__
        
        
        
        
