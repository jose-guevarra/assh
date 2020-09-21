"""
Class:  AsshConfig

"""
import os
import yaml
## AsshConfig object
#  config file gets created by package install
#  


class AsshConfig(object):
    'Handles running commands from alias info'
    Name = "AsshConfig"
    config = None
    configDir = '';
    
    def __init__(self):
        self.loadConfig()
        
    def loadConfig(self):
        userHomeDir = os.getenv('HOME')    # system dependent?
        if userHomeDir:
            self.configDir = userHomeDir + '/.local/share/assh'
            configFile = self.configDir + '/assh.yml'
        try:
            with open(configFile) as f:
                self.config = yaml.load(f)
        except IOError as e:
            print 'Configuration file not found:' + configFile
            sys.exit()
        
