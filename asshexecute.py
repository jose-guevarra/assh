::"
Class:  AsshExecute

"""


class AsshExecute(object):
    'Run command defined by alias'
    Name = "AsshExecute"

    
    def __init__(self, aliasObj):

        self.alias = aliasObj
        self.sshArgs = ['ssh']
        self.genCommand()

    def genCommand(self):

        if self.alias.bulkSshArgs is not None:
            self.sshArgs.append(self.alias.bulkSshArgs)
        
        if self.alias.sshUser is not None:
            tmp = self.alias.sshUser + '@'
            
        tmp = tmp + self.alias.sshHostname
        self.sshArgs.append(tmp)
        
    def connect(self):
        from subprocess import call
        #print self.sshArgs
        call(self.sshArgs)
        
        
        
